import subprocess
from pathlib import Path

class Camera:
    video_device: Path

    def __init__(self,video_device: Path):
        self.video_device = video_device

    def stream(self):
        ...

    def capture(self, width, height):
        v4l2_cmd = [
            "v4l2-ctl",
            f"--device={self.video_device}",
            f"--set-fmt-video=width={width},height={height},pixelformat=YUYV",
            "--stream-mmap",
            "--stream-count=1",
            "--stream-to=-",
        ]
        capture_image = subprocess.run(v4l2_cmd,stdout=subprocess.PIPE,check=True,)

        return capture_image.stdout

    def start_record(self):
        ...

    def stop_record(self):
        ...