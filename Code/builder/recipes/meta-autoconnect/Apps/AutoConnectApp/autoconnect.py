from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.config import Config
from kivy.core.window import Window
import os
import subprocess

class AutoConnect(App):
    def build(self):
        wPadding = (Window.size[0] / 16)
        wSpacing = (Window.size[0] / 16)
        widget_size_x = (Window.size[1] - (2 * wPadding) - wSpacing) / 2
        widget_size_y = (Window.size[1] - (2 * wPadding) - wSpacing) / 2

        root_widget = BoxLayout(orientation='vertical', padding=wPadding)
        
        button_grid = GridLayout(cols=3, spacing=[(Window.size[1] / 10.66) + (wPadding / 1.5), wSpacing])
        
        efi = Button(background_normal = 'EFI2.png', height=widget_size_y, width=widget_size_x, size_hint_x=None, size_hint_y=None)
        pe = Button(background_normal = 'PE.png', height=widget_size_y, width=widget_size_x, size_hint_x=None, size_hint_y=None)
        MegaLogViewer = Button(background_normal = 'MGLV.png', height=widget_size_y, width=widget_size_x, size_hint_x=None, size_hint_y=None)
        AndroidAuto = Button(background_normal = 'AndroidAuto.png', height=widget_size_y, width=widget_size_x, size_hint_x=None, size_hint_y=None)
        Settings = Button(background_normal = 'Settings.png', height=widget_size_y, width=widget_size_x, size_hint_x=None, size_hint_y=None)
        
        button_grid.add_widget(efi)
        button_grid.add_widget(pe)
        button_grid.add_widget(AndroidAuto)
        button_grid.add_widget(MegaLogViewer)
        button_grid.add_widget(Button(text="TBD", height=widget_size_y, width=widget_size_x, size_hint_x=None, size_hint_y=None))
        button_grid.add_widget(Settings)

        efi.bind(on_press = self.open_tuner_studio)
        MegaLogViewer.bind(on_press = self.open_mglv)

        root_widget.add_widget(button_grid)


        return root_widget
    
    def open_tuner_studio(self, event):
        os.system("open /Applications/TunerStudio_MS.app/")

    def open_mglv(self, event):
        #print("hi")
        subprocess.run(["open", "/Applications/MegaLogViewerHD.app/"])
        #os.system("open /Applications/MegaLogViewerHD.app/")

Window.fullscreen = True
AutoConnect().run()