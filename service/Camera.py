import av
import queue
import threading
import datetime
import time

from fractions import Fraction

class Camera:
    def __init__(self,video_source: str,video_format: str,audio_source: str | None = None,audio_format: str | None = None,audio_frequency: int = 48000,):
        self.video_source = video_source
        self.video_format = video_format
        self.audio_source = audio_source
        self.audio_format = audio_format
        self.audio_frequency = audio_frequency

        self.width = 0
        self.height = 0
        self.fps = 30

        self._video = None
        self._audio = None

        self._running = False
        self._recording = False

        self._video_thread = None
        self._audio_thread = None
        self._record_thread = None

        self._current_frame = None
        self._frame_lock = threading.Lock()

        self._record_lock = threading.Lock()
        self._record_queue = None
        self._record_start = 0

        self.recording_fileName = None

    def run(self, width=1920, height=1080, fps=30):
        if self._running:
            return

        self.width = width
        self.height = height
        self.fps = fps

        self._video = av.open(
            self.video_source,
            format=self.video_format,
            options={
                "video_size": f"{width}x{height}",
                "framerate": str(fps),
            },
        )
        if self.audio_source is not None:
            self._audio = av.open(self.audio_source,format=self.audio_format)

        self._running = True

        self._video_thread = threading.Thread(target=self._video_loop,daemon=True)
        self._video_thread.start()
        
        if self._audio:
            self._audio_thread = threading.Thread(target=self._audio_loop,daemon=True)
            self._audio_thread.start()

    def _video_loop(self):
        for frame in self._video.decode(video=0):

            if not self._running:
                break

            now = time.monotonic()

            with self._frame_lock:
                self._current_frame = frame

            self._submit("video", frame, now)

    def _audio_loop(self):

        for frame in self._audio.decode(audio=0):

            if not self._running:
                break

            self._submit("audio", frame, time.monotonic())

    def _submit(self, kind, frame, timestamp):
        with self._record_lock:
            if self._recording:
                self._record_queue.put((kind, frame, timestamp))

    def get_frame(self):
        with self._frame_lock:
            if self._current_frame is None:
                return None

            return self._current_frame.to_ndarray(format="rgb24")

    def capture(self):
        with self._frame_lock:
            if self._current_frame is None:
                raise RuntimeError("No frame available")
            frame = self._current_frame

        filename = (f"imageCapture_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.jpg")

        frame.to_image().save(filename)
        return filename

    def record(self):
        if not self._running:
            raise RuntimeError("Camera not running")

        with self._record_lock:
            if self._recording:
                raise RuntimeError("Recording already started")

            self.recording_fileName = (f"videoCapture_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.mp4")

            self._record_queue = queue.Queue()
            self._record_start = time.monotonic()
            self._recording = True

            self._record_thread = threading.Thread(
                target=self._record_loop,
                daemon=True,
            )
            self._record_thread.start()

        return self.recording_fileName

    def _record_loop(self):
        output = av.open(self.recording_fileName, "w")

        video = output.add_stream("libx264", rate=self.fps)
        video.width = self.width
        video.height = self.height
        video.pix_fmt = "yuv420p"

        audio = None
        resampler = None

        if self._audio:
            audio = output.add_stream("aac",rate=self.audio_frequency)
            audio.layout = "stereo"

            resampler = av.AudioResampler(
                format=audio.format.name,
                layout="stereo",
                rate=self.audio_frequency,
            )

        last_video_pts = -1
        audio_pts = None

        while True:
            item = self._record_queue.get()

            if item is None:
                break

            kind, frame, timestamp = item

            if kind == "video":

                frame = frame.reformat(self.width,self.height,format="yuv420p",)

                pts = int((timestamp - self._record_start) * self.fps)

                pts = max(pts, last_video_pts + 1)
                last_video_pts = pts

                frame.pts = pts
                frame.time_base = Fraction(1, self.fps)

                for packet in video.encode(frame):
                    output.mux(packet)

            elif kind == "audio" and audio:

                frames = resampler.resample(frame)

                for frame in frames:
                    if audio_pts is None:
                        audio_pts = max(0,int((timestamp - self._record_start) * self.audio_frequency))
                    frame.pts = audio_pts
                    frame.time_base = Fraction(
                        1,
                        self.audio_frequency,
                    )

                    audio_pts += frame.samples

                    for packet in audio.encode(frame):
                        output.mux(packet)

        for packet in video.encode(None):
            output.mux(packet)

        if audio:
            for packet in audio.encode(None):
                output.mux(packet)

        output.close()

    def end_record(self):
        with self._record_lock:

            if not self._recording:
                raise RuntimeError("Recording not started")

            self._recording = False
            self._record_queue.put(None)

        self._record_thread.join()

        self._record_thread = None
        self._record_queue = None


    def quit(self):
        if self._recording:
            self.end_record()

        if self._video:
            self._video.close()

        if self._audio:
            self._audio.close()

        self._running = False