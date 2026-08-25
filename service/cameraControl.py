import cv2
import Camera

class CameraControl:
    camera: Camera

    @classmethod
    def set_bightness(cls): # range 0 - 255
        ...

    @classmethod
    def set_contrast(cls): # range 0 - 255
        ...

    @classmethod
    def set_saturation(cls): # range 0 - 100
        ...

    @classmethod
    def set_hue(cls): # range -180 - 180
        ...

    @classmethod
    def set_white_balance_automatic(): # True or False
        ...

    @classmethod
    def set_gamma(cls): # range 90 - 150
        ...

    @classmethod
    def set_power_line_frequency(cls): # range 0 - 2
        ...

    @classmethod
    def setwhite_balance_temperature(cls): # range 2800 – 6500
        ...

    @classmethod
    def set_sharpness(cls): # range 0 - 7
        ...

