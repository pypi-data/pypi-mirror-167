from Paperl.Paperc import prWarring, prSuccess, prError
from typing import Literal


class Themes(object):
    def getDefaultStyle(self):
        from tkinter.ttk import Style
        return Style().theme_names()

    def useStyle(self, styleName):
        try:
            from tkinter.ttk import Style
            Style().theme_use(styleName)
        except:
            prWarring(f"Widget -> Style -> {styleName} -> This system does not support this theme")

    def useStyleAqua(self):
        self.useStyle("aqua")

    def useStyleVista(self):
        self.useStyle("vista")

    def useStyleWinNative(self):
        self.useStyle("winnative")

    def useStyleDefault(self):
        self.useStyle("default")

    def useStyleClassic(self):
        self.useStyle("classic")

    def useStyleAlt(self):
        self.useStyle("alt")

    def useStyleClam(self):
        self.useStyle("clam")

    def useStyleSunValley(self, Theme: Literal["light", "dark"] = "light"):
        try:
            from sv_ttk import use_dark_theme, use_light_theme
        except:
            prWarring("sv_ttk -> Check -> Not Installed")
        else:
            prSuccess("sv_ttk -> Check -> Installed")
            if Theme == "dark":
                use_dark_theme()
                self.setBackground("#1c1c1c")
            else:
                use_light_theme()
                self.setBackground("#fafafa")

    def useStyleEx(self, styleName):
        try:
            from ttkthemes import ThemedStyle
        except:
            prWarring("ttkthemes -> Check -> Not Installed")
        else:
            prSuccess("ttkthemes -> Check -> Installed")
            try:
                ThemedStyle(self.Me).theme_use(styleName)
            except:
                prError(f"ttkthemes -> {styleName} -> The theme could not be found")

    def useStyleExArc(self):
        self.useStyleEx("arc")

    def useStyleExEquilux(self):
        self.useStyleEx("equilux")

    def useStyleExWinXpBlue(self):
        self.useStyleEx("winxpblue")

    def useStyleExAquativo(self):
        self.useStyleEx("aquativo")

    def useStyleExAdapta(self):
        self.useStyleEx("adapta")

    def useStyleExBreeze(self):
        self.useStyleEx("breeze")

    def useStyleExRadiance(self):
        self.useStyleEx("radiance")

    def useStyleExYaru(self):
        self.useStyleEx("yaru")