from functools import singledispatch
from Paperl.Paperc import prWarring

try:
    from ctypes import Structure, c_int
except:
    pass
else:
    class Margins(Structure):
        _fields_ = [
            ("cxLeftWidth", c_int),
            ("cxRightWidth", c_int),
            ("cyTopHeight", c_int),
            ("cyBottomHeight", c_int),
        ]


class Windows22H2(object):
    def setSystemBackdropNone(self):
        try:
            self.windows_manage.dwm_set_window_attribute_systembackdrop_type_none()
        except:
            pass

    def setSystemBackdropAuto(self):
        try:
            self.windows_manage.dwm_set_window_attribute_systembackdrop_type_auto()
        except:
            pass

    def setSystemBackdropMainWindow(self):
        try:
            self.windows_manage.dwm_set_window_attribute_systembackdrop_type_mainwindow()
        except:
            pass

    def setSystemBackdropTabbedWindow(self):
        try:
            self.windows_manage.dwm_set_window_attribute_systembackdrop_type_tabbed_window()
        except:
            pass

    def setSystemBackdropTransientWindow(self):
        try:
            self.windows_manage.dwm_set_window_attribute_systembackdrop_type_transient_window()
        except:
            pass


class Windows21H2(object):
    def setDarkTheme(self):
        try:
            self.windows_manage.dwm_set_window_attribute_use_dark_mode()
        except:
            pass

    def setLightTheme(self):
        try:
            self.windows_manage.dwm_set_window_attribute_use_light_mode()
        except:
            pass

    @singledispatch
    def setBorderColor(self, hex: str):
        try:
            self.windows_manage.dwm_set_window_attribute_border_color(self.windows_manage.get_hex(hex))
        except:
            pass

    @setBorderColor.register(int)
    def setBorderColor(self, red, blue, green):
        try:
            self.windows_manage.dwm_set_window_attribute_border_color(self.windows_manage.get_rgb(red, blue, green))
        except:
            pass

    @singledispatch
    def setTitleColor(self, hex: str):
        try:
            self.windows_manage.dwm_set_window_attribute_text_color(self.windows_manage.get_hex(hex))
        except:
            pass

    @setTitleColor.register(int)
    def setTitleColor(self, red, blue, green):
        try:
            self.windows_manage.dwm_set_window_attribute_text_color(self.windows_manage.get_rgb(red, blue, green))
        except:
            pass

    def setRound(self):
        try:
            self.windows_manage.dwm_set_window_round_round()
        except:
            pass

    def setRoundSmall(self):
        try:
            self.windows_manage.dwm_set_window_round_round_small()
        except:
            pass

    def setRoundDoNot(self):
        try:
            self.windows_manage.dwm_set_window_round_donot_round()
        except:
            pass

    def setExtendFrameIntoClientArea(self, Left, Right, Top, Bottom):
        try:
            self.windows_manage.dwm_extend_frame_into_client_area((Left, Right, Top, Bottom))
        except TypeError:
            prWarring("Window -> TypeError -> Cannt set FrameBorderThickness")


class WindowsDev(Windows21H2, Windows22H2):
    pass