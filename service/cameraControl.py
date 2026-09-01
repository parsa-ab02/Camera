import cv2
from Camera import Camera
import subprocess

class CameraControl:
    def __init__(self, camera: Camera):
        self._camera = camera

    # BRIGHTNESS --- --- ---

    def set_brightness(self, value: int): # range 0 - 255
        if not 0 <= value <= 255:
            raise Exception("invalid brightness value")
        
        self._camera.set_property(
            cv2.CAP_PROP_BRIGHTNESS,
            value
        )

        return

    def get_brightness(self)->int:
        return self._camera.get_property(
            cv2.CAP_PROP_BRIGHTNESS
        )

    # CONTRAST --- --- ---
    
    def set_contrast(self, value: int): # range 0 - 255
        if not 0 <= value <= 255:
            raise Exception("invalid contrast value")
        
        self._camera.set_property(
            cv2.CAP_PROP_CONTRAST,
            value
        )

        return

    def get_contrast(self)->int:
        return self._camera.get_property(
            cv2.CAP_PROP_CONTRAST
        )

    # SATURATION --- --- ---

    def set_saturation(self, value: int): # range 0 - 100
        if not 0 <= value <= 100:
            raise Exception("invalid saturation value")

        self._camera.set_property(
            cv2.CAP_PROP_SATURATION,
            value
        )

    def get_saturation(self)->int:
        return self._camera.get_property(
            cv2.CAP_PROP_SATURATION
        )

    # HUE --- --- ---

    def set_hue(self, value: int): # range -180 - 180
        if not -180 <= value <= 180:
            raise Exception("invalid hue value")
        
        self._camera.set_property(
            cv2.CAP_PROP_HUE,
            value
        )

        return

    def get_hue(self)->int:
        return self._camera.get_property(
            cv2.CAP_PROP_HUE
        )

    # SHARPNESS --- --- ---

    def set_sharpness(self, value: int): # range 0 - 7
        if not 0 <= value <= 7:
            raise Exception("invalid sharpness value")
                
        self._camera.set_property(
            cv2.CAP_PROP_SHARPNESS,
            value
        )

        return

    def get_sharpness(self)->int:
        return self._camera.get_property(
            cv2.CAP_PROP_SHARPNESS
        )

    # GAMMA --- --- ---

    def set_gamma(self, value: int): # range 90 - 150
        if not 90 <= value <= 150:
            raise Exception("invalid gamma value")
                
        self._camera.set_property(
            cv2.CAP_PROP_GAMMA,
            value
        )

        return

    def get_gamma(self)->int:
        return self._camera.get_property(
            cv2.CAP_PROP_GAMMA
        )

    # AUTO WHITE BALANCE --- --- ---

    def set_white_balance_automatic(self, value: bool): # True or False
        self._camera.set_property(
            cv2.CAP_PROP_AUTO_WB,
            value
        )

        self._wb_automatic = bool

    def is_white_balance_automatic(self)->bool:
        return self._camera.get_property(
            cv2.CAP_PROP_AUTO_WB
        )

    # WHITE BALANCE TEMPERATURE --- --- ---

    def set_white_balance_temperature(self, value: int): # range 2800 – 6500
        if not self._wb_automatic:
            raise Exception("white balance automatic is set to auto")

        if not 2800 <= value <= 6500:
            raise Exception("invalid white balance temprature value")
                
        self._camera.set_property(
            cv2.CAP_PROP_WB_TEMPERATURE,
            value
        )

        return

    def get_white_balance_temperature(self)->int:
        return self._camera.get_property(
            cv2.CAP_PROP_BRIGHTNESS
        )

    # POWER LINE FREQUENCY --- --- ---

    # IMPORTANT NOTE : The following methods (power line frequency) will only work on linux devices with v4l2-ctl
    # The reason is the power line frequency (anti-flicker) setting is handled at the hardware or operating system driver level
    # If you are running this code on other OS, be careful !

    def set_power_line_frequency(self, value: int): # range 0 - 2
        if not 0 <= value <= 2:
            raise RuntimeError("invalid power line frequency value")

        if not isinstance(self._camera._video_source, str):
            return
        command = ["v4l2-ctl", "-d", str(self._camera._path), f"--set-ctrl=power_line_frequency={value}"]

        try:
            subprocess.run(command, capture_output=True, text=True, check=True)
        except(subprocess.CalledProcessError, FileNotFoundError) as e:
            raise RuntimeError(f"failed to set power line frequency : {e}") from e

        if self.get_power_line_frequency() != value:
            raise Exception("power line setting failed")

        return

    def get_power_line_frequency(self):
        if not isinstance(self._camera._video_source, str):
            return
        command = ["v4l2-ctl", "-d", str(self._camera._path), "--get-ctrl=power_line_frequency"]

        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
        except(subprocess.CalledProcessError, FileNotFoundError) as e:
            raise RuntimeError(f"failed to get power line frequency : {e}") from e

        try:
            return int(result.stdout.strip().split(":")[-1].strip())
        except (ValueError, IndexError) as e:
            raise RuntimeError(f"Unexpected v4l2-ctl output: {result.stdout!r}") from e