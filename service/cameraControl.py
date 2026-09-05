from Camera import Camera
import subprocess

class CameraControl:
    def __init__(self, camera: Camera):
        self._camera = camera

    # BRIGHTNESS --- --- ---

    def set_brightness(self, value: int): # range 0 - 255
        if not 0 <= value <= 255:
            raise Exception("invalid brightness value")
        
        command = ["v4l2-ctl", "-d", str(self._camera.video_source), f"--set-ctrl=brightness={value}"]

        try:
            subprocess.run(command, capture_output=True, text=True, check=True)
        except(subprocess.CalledProcessError, FileNotFoundError) as e:
            raise RuntimeError(f"failed to set brightness : {e}") from e

        return

    def get_brightness(self)->int:
        command = ["v4l2-ctl", "-d", str(self._camera.video_source), "--get-ctrl=brightness"]

        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
        except(subprocess.CalledProcessError, FileNotFoundError) as e:
            raise RuntimeError(f"failed to get brightness : {e}") from e

        try:
            return int(result.stdout.strip().split(":")[-1].strip())
        except (ValueError, IndexError) as e:
            raise RuntimeError(f"Unexpected v4l2-ctl output: {result.stdout!r}") from e

    # CONTRAST --- --- ---
    
    def set_contrast(self, value: int): # range 0 - 255
        if not 0 <= value <= 255:
            raise Exception("invalid contrast value")
        
        command = ["v4l2-ctl", "-d", str(self._camera.video_source), f"--set-ctrl=contrast={value}"]

        try:
            subprocess.run(command, capture_output=True, text=True, check=True)
        except(subprocess.CalledProcessError, FileNotFoundError) as e:
            raise RuntimeError(f"failed to set contrast : {e}") from e

        return

    def get_contrast(self)->int:
        command = ["v4l2-ctl", "-d", str(self._camera.video_source), "--get-ctrl=contrast"]

        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
        except(subprocess.CalledProcessError, FileNotFoundError) as e:
            raise RuntimeError(f"failed to get contrast : {e}") from e

        try:
            return int(result.stdout.strip().split(":")[-1].strip())
        except (ValueError, IndexError) as e:
            raise RuntimeError(f"Unexpected v4l2-ctl output: {result.stdout!r}") from e

    # SATURATION --- --- ---

    def set_saturation(self, value: int): # range 0 - 100
        if not 0 <= value <= 100:
            raise Exception("invalid saturation value")

        command = ["v4l2-ctl", "-d", str(self._camera.video_source), f"--set-ctrl=saturation={value}"]

        try:
            subprocess.run(command, capture_output=True, text=True, check=True)
        except(subprocess.CalledProcessError, FileNotFoundError) as e:
            raise RuntimeError(f"failed to set saturation : {e}") from e

    def get_saturation(self)->int:
        command = ["v4l2-ctl", "-d", str(self._camera.video_source), "--get-ctrl=saturation"]

        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
        except(subprocess.CalledProcessError, FileNotFoundError) as e:
            raise RuntimeError(f"failed to get saturation : {e}") from e

        try:
            return int(result.stdout.strip().split(":")[-1].strip())
        except (ValueError, IndexError) as e:
            raise RuntimeError(f"Unexpected v4l2-ctl output: {result.stdout!r}") from e

    # HUE --- --- ---

    def set_hue(self, value: int): # range -180 - 180
        if not -180 <= value <= 180:
            raise Exception("invalid hue value")
        
        command = ["v4l2-ctl", "-d", str(self._camera.video_source), f"--set-ctrl=hue={value}"]

        try:
            subprocess.run(command, capture_output=True, text=True, check=True)
        except(subprocess.CalledProcessError, FileNotFoundError) as e:
            raise RuntimeError(f"failed to set hue : {e}") from e

        return

    def get_hue(self)->int:
        command = ["v4l2-ctl", "-d", str(self._camera.video_source), "--get-ctrl=hue"]

        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
        except(subprocess.CalledProcessError, FileNotFoundError) as e:
            raise RuntimeError(f"failed to get hue : {e}") from e

        try:
            return int(result.stdout.strip().split(":")[-1].strip())
        except (ValueError, IndexError) as e:
            raise RuntimeError(f"Unexpected v4l2-ctl output: {result.stdout!r}") from e

    # SHARPNESS --- --- ---

    def set_sharpness(self, value: int): # range 0 - 7
        if not 0 <= value <= 7:
            raise Exception("invalid sharpness value")
                
        command = ["v4l2-ctl", "-d", str(self._camera.video_source), f"--set-ctrl=sharpness={value}"]

        try:
            subprocess.run(command, capture_output=True, text=True, check=True)
        except(subprocess.CalledProcessError, FileNotFoundError) as e:
            raise RuntimeError(f"failed to set sharpness : {e}") from e

        return

    def get_sharpness(self)->int:
        command = ["v4l2-ctl", "-d", str(self._camera.video_source), "--get-ctrl=sharpness"]

        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
        except(subprocess.CalledProcessError, FileNotFoundError) as e:
            raise RuntimeError(f"failed to get sharpness : {e}") from e

        try:
            return int(result.stdout.strip().split(":")[-1].strip())
        except (ValueError, IndexError) as e:
            raise RuntimeError(f"Unexpected v4l2-ctl output: {result.stdout!r}") from e

    # GAMMA --- --- ---

    def set_gamma(self, value: int): # range 90 - 150
        if not 90 <= value <= 150:
            raise Exception("invalid gamma value")
                
        command = ["v4l2-ctl", "-d", str(self._camera.video_source), f"--set-ctrl=gamma={value}"]

        try:
            subprocess.run(command, capture_output=True, text=True, check=True)
        except(subprocess.CalledProcessError, FileNotFoundError) as e:
            raise RuntimeError(f"failed to set gamma : {e}") from e

        return

    def get_gamma(self)->int:
        command = ["v4l2-ctl", "-d", str(self._camera.video_source), "--get-ctrl=gamma"]

        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
        except(subprocess.CalledProcessError, FileNotFoundError) as e:
            raise RuntimeError(f"failed to get gamma : {e}") from e

        try:
            return int(result.stdout.strip().split(":")[-1].strip())
        except (ValueError, IndexError) as e:
            raise RuntimeError(f"Unexpected v4l2-ctl output: {result.stdout!r}") from e

    # AUTO WHITE BALANCE --- --- ---

    def set_white_balance_automatic(self, value: bool): # True or False
        command = ["v4l2-ctl", "-d", str(self._camera.video_source), f"--set-ctrl=white_balance_automatic={int(value)}"]

        try:
            subprocess.run(command, capture_output=True, text=True, check=True)
        except(subprocess.CalledProcessError, FileNotFoundError) as e:
            raise RuntimeError(f"failed to set automatic white balance : {e}") from e

        self._wb_automatic = bool

    def is_white_balance_automatic(self)->bool:
        command = ["v4l2-ctl", "-d", str(self._camera.video_source), "--get-ctrl=white_balance_automatic"]

        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
        except(subprocess.CalledProcessError, FileNotFoundError) as e:
            raise RuntimeError(f"failed to get automatic white balance : {e}") from e

        try:
            return bool(int(result.stdout.strip().split(":")[-1].strip()))
        except (ValueError, IndexError) as e:
            raise RuntimeError(f"Unexpected v4l2-ctl output: {result.stdout!r}") from e

    # WHITE BALANCE TEMPERATURE --- --- ---

    def set_white_balance_temperature(self, value: int): # range 2800 – 6500
        if not self._wb_automatic:
            raise Exception("white balance automatic is set to auto")

        if not 2800 <= value <= 6500:
            raise Exception("invalid white balance temprature value")
                
        command = ["v4l2-ctl", "-d", str(self._camera.video_source), f"--set-ctrl=white_balance_temperature={value}"]

        try:
            subprocess.run(command, capture_output=True, text=True, check=True)
        except(subprocess.CalledProcessError, FileNotFoundError) as e:
            raise RuntimeError(f"failed to set white balance temperature : {e}") from e

        return

    def get_white_balance_temperature(self)->int:
        command = ["v4l2-ctl", "-d", str(self._camera.video_source), "--get-ctrl=white_balance_temperature"]

        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
        except(subprocess.CalledProcessError, FileNotFoundError) as e:
            raise RuntimeError(f"failed to get white balance temperature : {e}") from e

        try:
            return int(result.stdout.strip().split(":")[-1].strip())
        except (ValueError, IndexError) as e:
            raise RuntimeError(f"Unexpected v4l2-ctl output: {result.stdout!r}") from e

    # POWER LINE FREQUENCY --- --- ---

    def set_power_line_frequency(self, value: int): # range 0 - 2
        if not 0 <= value <= 2:
            raise RuntimeError("invalid power line frequency value")

        if not isinstance(self._camera.video_source, str):
            return
        command = ["v4l2-ctl", "-d", str(self._camera.video_source), f"--set-ctrl=power_line_frequency={value}"]

        try:
            subprocess.run(command, capture_output=True, text=True, check=True)
        except(subprocess.CalledProcessError, FileNotFoundError) as e:
            raise RuntimeError(f"failed to set power line frequency : {e}") from e

        if self.get_power_line_frequency() != value:
            raise Exception("power line setting failed")

        return

    def get_power_line_frequency(self):
        if not isinstance(self._camera.video_source, str):
            return
        command = ["v4l2-ctl", "-d", str(self._camera.video_source), "--get-ctrl=power_line_frequency"]

        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
        except(subprocess.CalledProcessError, FileNotFoundError) as e:
            raise RuntimeError(f"failed to get power line frequency : {e}") from e

        try:
            return int(result.stdout.strip().split(":")[-1].strip())
        except (ValueError, IndexError) as e:
            raise RuntimeError(f"Unexpected v4l2-ctl output: {result.stdout!r}") from e