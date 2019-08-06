from kivy.app import App
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

import time

Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '480')


class V3Widget(BoxLayout):
    pass


class ClockLabel(Label):
    def __init__(self, **kwargs):
        super(ClockLabel, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1)

    def update(self, *args):
        self.text = time.strftime('%I:%M %p')


class V3App(App):
    def build(self):
        return V3Widget()


if __name__ == "__main__":
    V3App().run()
