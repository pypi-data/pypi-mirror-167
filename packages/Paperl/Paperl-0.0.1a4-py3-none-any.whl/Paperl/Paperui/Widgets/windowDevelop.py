from functools import singledispatch
from Paperl.Paperc import prWarring, prSuccess, prError

try:
    from ctypes import Structure, c_int, POINTER, pointer, sizeof
    from ctypes.wintypes import DWORD, ULONG
    import ctypes
except:
    pass
else:
    class AccentPolicy(Structure):
        """ 设置客户区的具体属性 """
        _fields_ = [
            ('AccentState', DWORD),
            ('AccentFlags', DWORD),
            ('GradientColor', DWORD),
            ('AnimationId', DWORD),
        ]


    class WindowCompositionAttribute(Structure):
        _fields_ = [
            ('Attribute', DWORD),
            ('Data', POINTER(AccentPolicy)),  # POINTER()接收任何ctypes类型，并返回一个指针类型
            ('SizeOfData', ULONG),
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

    def useMica(self, theme="light"):
        try:
            from win32mica import ApplyMica
        except:
            prWarring("win32mica -> Check -> Not Installed")
        else:
            try:
                if theme == "dark":
                    ApplyMica(self.gethWnd(), True)
                else:
                    ApplyMica(self.gethWnd(), False)
            except:
                prWarring("win32mica -> Use -> Cannot be used normally")

    @singledispatch
    def setCaptionColor(self, hex: str):
        try:
            self.windows_manage.dwm_set_window_attribute_caption_color(self.windows_manage.get_hex(hex))
        except:
            pass

    @setCaptionColor.register(int)
    def setCaptionColor(self, red, blue, green):
        try:
            self.windows_manage.dwm_set_window_attribute_caption_color(self.windows_manage.get_rgb(red, blue, green))
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


class WindowsEffect(object):
    def __init__(self):
        self.ACCENT_DISABLED = 0,
        self.ACCENT_ENABLE_GRADIENT = 1,
        self.ACCENT_ENABLE_TRANSPARENTGRADIENT = 2,
        self.ACCENT_ENABLE_BLURBEHIND = 3,  # Aero效果
        self.ACCENT_ENABLE_ACRYLICBLURBEHIND = 4,  # 亚克力效果
        self.ACCENT_INVALID_STATE = 5

        self.WCA_UNDEFINED = 0,
        self.WCA_NCRENDERING_ENABLED = 1,
        self.WCA_NCRENDERING_POLICY = 2,
        self.WCA_TRANSITIONS_FORCEDISABLED = 3,
        self.WCA_ALLOW_NCPAINT = 4,
        self.WCA_CAPTION_BUTTON_BOUNDS = 5,
        self.WCA_NONCLIENT_RTL_LAYOUT = 6,
        self.WCA_FORCE_ICONIC_REPRESENTATION = 7,
        self.WCA_EXTENDED_FRAME_BOUNDS = 8,
        self.WCA_HAS_ICONIC_BITMAP = 9,
        self.WCA_THEME_ATTRIBUTES = 10,
        self.WCA_NCRENDERING_EXILED = 11,
        self.WCA_NCADORNMENTINFO = 12,
        self.WCA_EXCLUDED_FROM_LIVEPREVIEW = 13,
        self.WCA_VIDEO_OVERLAY_ACTIVE = 14,
        self.WCA_FORCE_ACTIVEWINDOW_APPEARANCE = 15,
        self.WCA_DISALLOW_PEEK = 16,
        self.WCA_CLOAK = 17,
        self.WCA_CLOAKED = 18,
        self.WCA_ACCENT_POLICY = 19,
        self.WCA_FREEZE_REPRESENTATION = 20,
        self.WCA_EVER_UNCLOAKED = 21,
        self.WCA_VISUAL_OWNER = 22,
        self.WCA_LAST = 23

    def useAcrylic(self, theme="light"):
        try:
            from BlurWindow.blurWindow import GlobalBlur
        except:
            prWarring("BlurWindow -> Check -> Not Installed")
        else:
            prSuccess("BlurWindow -> Check -> Installed")
            try:
                if theme == "dark":
                    GlobalBlur(self.gethWnd(), Dark=True)
                else:
                    GlobalBlur(self.gethWnd(), Dark=False)
            except:
                prWarring("BlurWindow -> Use -> Cannot be used normally")

    def setWindowCompositionAttribute(self, Attribute):
        try:
            self.SetWindowCompositionAttribute(self.gethWnd(), Attribute)
        except:
            prError("Widget -> SetWindowCompositionAttribute -> Error")

    def setAccent(self, Accent):
        try:
            self.AccentPolicy = AccentPolicy()
            self.AccentPolicy.AccentState = Accent
        except:
            pass
        try:
            import ctypes
            self.WindowCompAttributeData = WindowCompositionAttribute()
            self.WindowCompAttributeData.Attribute = 19
            self.WindowCompAttributeData.SizeOfData = sizeof(self.AccentPolicy)
            self.WindowCompAttributeData.Data = pointer(self.AccentPolicy)
            ctypes.windll.user32.SetWindowCompositionAttribute(self.gethWnd(), pointer(self.WindowCompAttributeData))
        except TypeError:
            prError("Widget -> SetAccent -> Error")

    def useEnableGradient(self):
        self.setAccent(1)

    def useEnableTransparentGradient(self):
        self.setAccent(2)

    def useEnableBlurBehind(self):
        self.setAccent(3)

    def useEnableAcrylicBlurBehind(self):
        self.setAccent(4)

    def useAero(self):
        self.useEnableBlurBehind()


class WindowsDev(Windows21H2, Windows22H2, WindowsEffect):
    pass