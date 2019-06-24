from kivy.app import App

from kivy.config import Config
# remove red dot on mouse2
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('kivy', 'desktop', 1)
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'borderless', 0)
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import OptionProperty
from kivy.uix.behaviors import focus

Window.on_keyboard(Window.maximize())

class Interface(Widget):
    Window.size = (450, 250)

    tab = OptionProperty("normal", options=["normal", "down"])
    q = OptionProperty("normal", options=["normal", "down"])
    w = OptionProperty("normal", options=["normal", "down"])
    e = OptionProperty("normal", options=["normal", "down"])
    r = OptionProperty("normal", options=["normal", "down"])
    a = OptionProperty("normal", options=["normal", "down"])
    s = OptionProperty("normal", options=["normal", "down"])
    d = OptionProperty("normal", options=["normal", "down"])
    f = OptionProperty("normal", options=["normal", "down"])
    g = OptionProperty("normal", options=["normal", "down"])
    shift = OptionProperty("normal", options=["normal", "down"])
    z = OptionProperty("normal", options=["normal", "down"])
    xx = OptionProperty("normal", options=["normal", "down"])
    c = OptionProperty("normal", options=["normal", "down"])
    lctrl = OptionProperty("normal", options=["normal", "down"])
    alt = OptionProperty("normal", options=["normal", "down"])
    spacebar = OptionProperty("normal", options=["normal", "down"])

    def __init__(self, **kwargs):
        super(Interface, self).__init__(**kwargs)
        self.keyboard = Window.request_keyboard(self.keyboard_closed, self)
        self.keyboard.bind(on_key_down=self.on_keyboard_down)
        self.keyboard.bind(on_key_up=self.on_keyboard_up)

    def on_maximize(self):
        if self.collide_widget(Interface):
            focus.FocusBehavior.focused()

    def keyboard_closed(self):
        self.keyboard.unbind(on_key_down=self.on_keyboard_down)
        self.keyboard.unbind(on_key_up=self.on_keyboard_up)
        self.keyboard = None

    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == "w":
            print("{} was pressed".format(keycode[1]))
            self.w = "down"
            return True
        elif keycode[1] == "tab":
            print("{} was pressed".format(keycode[1]))
            self.tab = "down"
            return True
        elif keycode[1] == "q":
            print("{} was pressed".format(keycode[1]))
            self.q = "down"
            return True
        elif keycode[1] == "e":
            print("{} was pressed".format(keycode[1]))
            self.e = "down"
            return True
        elif keycode[1] == "r":
            print("{} was pressed".format(keycode[1]))
            self.r = "down"
            return True
        elif keycode[1] == "a":
            print("{} was pressed".format(keycode[1]))
            self.a = "down"
            return True
        elif keycode[1] == "s":
            print("{} was pressed".format(keycode[1]))
            self.s = "down"
            return True
        elif keycode[1] == "d":
            print("{} was pressed".format(keycode[1]))
            self.d = "down"
            return True
        elif keycode[1] == "f":
            print("{} was pressed".format(keycode[1]))
            self.f = "down"
            return True
        elif keycode[1] == "g":
            print("{} was pressed".format(keycode[1]))
            self.g = "down"
            return True
        elif keycode[1] == "shift":
            print("{} was pressed".format(keycode[1]))
            self.shift = "down"
            return True
        elif keycode[1] == "z":
            print("{} was pressed".format(keycode[1]))
            self.z = "down"
            return True
        elif keycode[1] == "x":
            print("{} was pressed".format(keycode[1]))
            self.xx = "down"
            return True
        elif keycode[1] == "c":
            print("{} was pressed".format(keycode[1]))
            self.c = "down"
            return True
        elif keycode[1] == "lctrl":
            print("{} was pressed".format(keycode[1]))
            self.lctrl = "down"
            return True
        elif keycode[1] == "alt":
            print("{} was pressed".format(keycode[1]))
            self.alt = "down"
            return True
        elif keycode[1] == "spacebar":
            print("{} was pressed".format(keycode[1]))
            self.spacebar = "down"
            return True
        else:
            return "error"

    def on_keyboard_up(self, keyboard, keycode):
        if keycode[1] == "w":
            print("{} was released".format(keycode[1]))
            self.w = "normal"
            return True
        elif keycode[1] == "tab":
            print("{} was released".format(keycode[1]))
            self.tab = "normal"
            return True
        elif keycode[1] == "q":
            print("{} was released".format(keycode[1]))
            self.q = "normal"
            return True
        elif keycode[1] == "e":
            print("{} was released".format(keycode[1]))
            self.e = "normal"
            return True
        elif keycode[1] == "r":
            print("{} was released".format(keycode[1]))
            self.r = "normal"
            return True
        elif keycode[1] == "a":
            print("{} was released".format(keycode[1]))
            self.a = "normal"
            return True
        elif keycode[1] == "s":
            print("{} was released".format(keycode[1]))
            self.s = "normal"
            return True
        elif keycode[1] == "d":
            print("{} was released".format(keycode[1]))
            self.d = "normal"
            return True
        elif keycode[1] == "f":
            print("{} was released".format(keycode[1]))
            self.f = "normal"
            return True
        elif keycode[1] == "g":
            print("{} was released".format(keycode[1]))
            self.g = "normal"
            return True
        elif keycode[1] == "shift":
            print("{} was released".format(keycode[1]))
            self.shift = "normal"
            return True
        elif keycode[1] == "z":
            print("{} was released".format(keycode[1]))
            self.z = "normal"
            return True
        elif keycode[1] == "x":
            print("{} was released".format(keycode[1]))
            self.xx = "normal"
            return True
        elif keycode[1] == "c":
            print("{} was released".format(keycode[1]))
            self.c = "normal"
            return True
        elif keycode[1] == "lctrl":
            print("{} was released".format(keycode[1]))
            self.lctrl = "normal"
            return True
        elif keycode[1] == "alt":
            print("{} was released".format(keycode[1]))
            self.alt = "normal"
            return True
        elif keycode[1] == "spacebar":
            print("{} was released".format(keycode[1]))
            self.spacebar = "normal"
            return True
        else:
            return "error"


class KpUI(App):
    def build(self):
        self.title = "KpUI"
        return Interface()


if __name__ == "__main__":
    KpUI().run()

