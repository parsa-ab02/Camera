import cv2
import Camera

class CameraControl:
    def __init__(self, camera:Camera):
        self._camera = camera

    def set_brightness(self, value: int): # range 0 - 255
        if not 0 <= value <= 255:
            raise Exception("invalid brightness value")
        
        self._camera.set_property(
            cv2.CAP_PROP_BRIGHTNESS,
            value
        )

        return
    
    def set_contrast(self, value: int): # range 0 - 255
        if not 0 <= value <= 255:
            raise Exception("invalid contrast value")
        
        self._camera.set_property(
            cv2.CAP_PROP_CONTRAST,
            value
        )

    def set_saturation(self, value: int): # range 0 - 100
        if not 0 <= value <= 100:
            raise Exception("invalid saturation value")

        self._camera.set_property(
            cv2.CAP_PROP_SATURATION,
            value
        )

    def set_hue(self, value: int): # range -180 - 180
        if not -180 <= value <= 180:
            raise Exception("invalid hue value")
        
        self._camera.set_property(
            cv2.CAP_PROP_HUE,
            value
        )

    def set_white_balance_automatic(self, value: bool): # True or False
        self._camera.set_property(
            cv2.CAP_PROP_AUTO_WB,
            value
        )

    def set_gamma(self, value: int): # range 90 - 150
        if not 90 <= value <= 150:
            raise Exception("invalid gamma value")
                
        self._camera.set_property(
            cv2.CAP_PROP_GAMMA,
            value
        )

    def set_white_balance_temperature(self, value: int): # range 2800 – 6500
        if not 2800 <= value <= 6500:
            raise Exception("invalid white balance temprature value")
                
        self._camera.set_property(
            cv2.CAP_PROP_WB_TEMPERATURE,
            value
        )

    def set_sharpness(self, value: int): # range 0 - 7
        if not 0 <= value <= 7:
            raise Exception("invalid sharpness value")
                
        self._camera.set_property(
            cv2.CAP_PROP_SHARPNESS,
            value
        )

    # def set_power_line_frequency(self, value: int): # range 0 - 2
        #     if not 0 <= value <= 2:
        #         raise Exception("invalid power line frequency value")
                    
        #     self._camera.set_property(
        #         cv2.CAP_PROP_,
        #         value
        #     )