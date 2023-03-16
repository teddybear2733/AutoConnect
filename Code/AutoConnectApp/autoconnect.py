from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ListProperty, NumericProperty
from kivy.graphics import *
import os
import time
from threading import Thread
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

    def open_app(self, app_path):
        thread = Thread(target=self.task,  args=(app_path,))
        thread.start()

    def task(self, app_path):
        applicationsFolder = os.path.join(os.path.dirname(__file__), "Applications")
        appLaunchScript = os.path.join(applicationsFolder, app_path)
        os.system(appLaunchScript)
        #self.manager.current = "MainMenu"

class SettingsScreen(Screen):
    #bckColor = (30/255, 30/255, 30/255, 255/255)

    def change_color(self):
        pass
        #print(self.bckColor)
        #self.bckColor = (1,1,1,1)
        #print(self.bckColor)

class LoadingScreen(Screen):
    
    pass
        
    

class TestApp(App):

    def switch_screens(self):
        pass

    def build(self):
        # Create the screen manager
        self.sm = ScreenManager()

        # Dark Mode
        self.sm.add_widget(MenuScreen(name='MainMenu'))
        self.sm.add_widget(LoadingScreen(name='Loading'))
        self.sm.add_widget(SettingsScreen(name='Settings'))

        # Light Mode
        # self.sm.add_widget(MenuScreenLight(name='MainMenuLight'))
        # self.sm.add_widget(LoadingScreenLight(name='LoadingLight'))
        # self.sm.add_widget(SettingsScreenLight(name='SettingsLight'))

        return self.sm

if __name__ == '__main__':
    #Window.fullscreen = True

    TestApp().run()
    