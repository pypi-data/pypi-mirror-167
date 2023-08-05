from Paperl.Paperui.Widgets.constant import *
from Paperl.Paperc import prDebugging, prError


class EventHandle(object):
    def __init__(self):
        self.build()

    def build(self):
        from tkinter import Widget
        try:
            self.Me = Widget()
        except:
            pass

    def waitEvent(self, eventTime: int, eventFunc: None = ...):
        try:
            self.Me.after(eventTime, eventFunc)
        except:
            prError("Widget -> Bind -> Please confirm whether the eventTime is correct or the eventFunc is wrong")

    def bindEvent(self, eventName=None, eventFunc: None = ...):
        try:
            self.Me.bind(eventName, eventFunc)
        except:
            prError("Widget -> Bind -> Please confirm whether the eventName is correct or the eventFunc is wrong")

    def onEnter(self, eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onEnter")
        self.bindEvent(EVENT_ENTER, eventFunc)

    def onLeave(self, eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onLeave")
        self.bindEvent(EVENT_LEAVE, eventFunc)

    def onButtonLeft(self, eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onButtonLeft")
        self.bindEvent(EVENT_BUTTON1, eventFunc)

    def onButtonMiddle(self, eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onButtonMiddle")
        self.bindEvent(EVENT_BUTTON2, eventFunc)

    def onButtonRight(self, eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onButtonRight")
        self.bindEvent(EVENT_BUTTON3, eventFunc)

    def onButtonAll(self, eventFunc: None = ...):
        prDebugging("Widget -> Bind -> onButtonAll")
        self.bindEvent(EVENT_BUTTON_ALL, eventFunc)
