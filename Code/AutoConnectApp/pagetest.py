from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import *
import os
# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_file('screens.kv')

            

# Declare both screens
class MenuScreen(Screen):

    wPadding = (Window.size[0] / 16)
    wSpacingx = (Window.size[1] / 10.66) + (wPadding / 1.5)
    wSpacingy = (Window.size[0] / 16)
    widget_size_x = (Window.size[1] - (2 * wPadding) - wSpacingx) / 2
    widget_size_y = (Window.size[1] - (2 * wPadding) - wSpacingx) / 2

    def open_tuner_studio(self):
        pass
        #os.system("open /Applications/TunerStudio_MS.app/")


class SettingsScreen(Screen):
    
    bckColor = (30/255, 30/255, 30/255, 255/255)

    def changeColor(self, color=1):
        print(color)
        
    

class TestApp(App):

    def switch_screens(self):
        pass

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='MainMenu'))
        sm.add_widget(SettingsScreen(name='Settings'))

        return sm

if __name__ == '__main__':
    Window.fullscreen = True
    TestApp().run()