import cv2
import threading
import datetime

class Camera:
    def __init__(self, camera_id=0):
        self._camera: cv2.VideoCapture | None = cv2.VideoCapture(camera_id)

        self._is_recording: bool = False
        self._is_streaming: bool = False

        self._writer: cv2.VideoWriter | None = None

        self._current_ret: bool = False
        self._current_frame: cv2.typing.MatLike | None = None

        self.recording_fileName: str | None = None

    def run(self, width, height, fps=30):
        self._camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self._camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self._camera.set(cv2.CAP_PROP_FPS, fps)

        self.width = int(self._camera.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self._camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.fps = fps

        self.streamThread = threading.Thread(
            target=self._stream,
        )

        self.streamThread.start()

    def _stream(self):
        self._is_streaming = True

        while self._is_streaming:
            self._current_ret, self._current_frame = self._camera.read()
            if not self._current_ret:
                raise Exception("video device not working")

            if self._is_recording and self._writer is not None:
                self._writer.write(self._current_frame)

            cv2.imshow("camera", self._current_frame)
            cv2.waitKey(1)

        return

    def quit(self):
        self._is_streaming = False

        if self._is_recording:
            self.end_record()

        if self._camera is not None:
            self._camera.release()

        cv2.destroyAllWindows()

    def capture(self):
        if not self._current_ret:
            raise Exception("no frame available")

        fileName = f"imageCapture_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.jpg"

        cv2.imwrite(
            filename=fileName,
            img=self._current_frame.copy()
        )

        

    def record(self):
        if self._is_recording:
            raise RuntimeError("recording already started")
        
        fileName = f"videoCapture_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.avi"

        fourcc = cv2.VideoWriter_fourcc(*'XVID')

        writer = cv2.VideoWriter(
            filename=fileName,
            fourcc=fourcc,
            fps=self.fps,
            frameSize=(self.width,self.height),
        )

        if not writer.isOpened():
            writer.release()
            raise RuntimeError("could not create video file")

        self._writer = writer
        self._is_recording = True

    def end_record(self):
        if self._is_recording:

            self._is_recording = False
            self._writer.release()

            self._writer = None

        else :
            raise Exception("recording not started")
        