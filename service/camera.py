import cv2
import threading
import time

class Camera:
    _camera: cv2.VideoCapture
    _is_recording: bool
    _is_streaming: bool

    _video: list
    _history: list

    def __init__(self, camera_id):
        self._camera = cv2.VideoCapture(camera_id)
        self._is_recording = False
        self._is_streaming = False

        self._video = []
        self._history = []

    def run(self, width, height, fps):
        self.streamThread = threading.Thread(
            target=self._stream,
            args=(width, height, fps)
        )

        self.streamThread.start()

    def _stream(self, width, height, fps):
        self._is_streaming = True

        frame_time = 1 / fps

        while self._is_streaming:
            start = time.perf_counter()

            ret, frame = self._camera.read()
            if not ret:
                raise Exception

            if self._is_recording:
                self._video.append((ret, frame))

            cv2.imshow("camera", frame)

            delay = frame_time - (time.perf_counter()-start)

            if  delay > 0:
                time.sleep(delay)

        return

    def quit(self):
        self._is_streaming = False

    def capture(self):
        ret, image = self._camera.read()

        if not ret:
            raise Exception

        self._history.append(image)

    def record(self):
        self._is_recording = True

    def end_record(self):
        self._is_recording = False
        self._history.append(self._video)
        self._video = []

    def save():
        for item in _history:
            ...
        