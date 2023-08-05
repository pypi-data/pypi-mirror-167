from Paperl.Paperui.Widgets.widget import Widget
from Paperl.Paperui.Widgets.windowDevelop import WindowsDev
from Paperl.Paperui.Widgets.themes import Themes
from Paperl.Paperc import prDebugging, prError, prSuccess
from functools import singledispatch
from typing import Literal


class Window(Widget, WindowsDev, Themes):
    __name__ = "Window"

    def __init__(self):
        self.build()
        self.init()
        try:
            from tkdev4 import DevManage
        except:
            pass
        else:
            try:
                self.windows_manage = DevManage(self.Me)
            except:
                pass
        self.setSystemBackdropNone()

    def build(self) -> None:
        from tkinter import Tk
        self.Me = Tk()
        prDebugging("Window -> Build")

    def init(self) -> None:
        self.setEmptyIcon()
        self.setBackground("#fafafa")
        self.setTitle("Paperl")
        self.setSize(250, 250)

    def setIcon(self, image):
        self.Me.iconbitmap(image)

    def setEmptyIcon(self):
        try:
            import tempfile
            empty_icon = (b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x08\x00h\x05\x00\x00'
                          b'\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00'
                          b'\x08\x00\x00\x00\x00\x00@\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                          b'\x00\x01\x00\x00\x00\x01') + b'\x00' * 1282 + b'\xff' * 64
            _, empty_icon_path = tempfile.mkstemp()
            with open(empty_icon_path, 'wb') as empty_icon_file:
                empty_icon_file.write(empty_icon)
            self.setIcon(empty_icon_path)
        except:
            pass

    def setTitle(self, title: str) -> None:
        self.Me.title(title)

    def setText(self, text: str):
        from tkinter import TclError
        try:
            self.setTitle(text)
        except TclError:
            prError("Window -> Text -> This property is not supported or this value is not supported")

    def getTitle(self) -> str:
        return self.Me.title()

    def setGeometry(self, width: int, height: int, x: int, y: int) -> None:
        self.Me.geometry(f"{str(width)}x{str(height)}+{str(x)}+{str(y)}")

    def getGeometry(self):
        return self.getSize(), self.getPosition()

    def setSize(self, width: int, height: int) -> None:
        self.Me.geometry(f"{str(width)}x{str(height)}")

    def setPosition(self, x: int, y: int) -> None:
        self.Me.geometry(f"+{str(x)}+{str(y)}")

    def bell(self):
        self.Me.bell()

    def mainLoop(self) -> None:
        try:
            prDebugging("Window -> MainLoop")
        except:
            prError("Window -> MainLoop -> Error")
        try:
            self.Me.mainloop()
        except:
            prError("Window -> Run -> Error")
        prDebugging("Window -> Quit")
