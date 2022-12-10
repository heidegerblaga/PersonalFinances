from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
import requests
from start import main
import analysis as al
from kivy.uix.label import Label
import time


# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
kv = Builder.load_file("PersonalFinance.kv")

# Declare both screens


class Menu(Screen):
    def main(self):
        self.main = main

    pass


class Scan(Screen):

        def capture(self):
            '''
            Function to capture the images and give them the names
            according to their captured time and date.
            '''
            camera = self.ids['camera']
            timestr = time.strftime("%Y%m%d_%H%M%S")
            camera.export_to_png("C:/Users/skyri/PycharmProjects/PersonalFinances/folder/IMG_{}.png".format(timestr))
            print("Captured")

class Analys(Screen):
    def navigator(self,args):
     self.navigator = al.navigator(args)



    pass


class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")


class TestApp(App):
    firebas_url = "https://personal-finanse-default-rtdb.europe-west1.firebasedatabase.app/.json"
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(Menu(name='menu'))
        sm.add_widget(Scan(name='scan'))
        sm.add_widget(Analys(name='analys'))

        return sm

if __name__ == '__main__':
    TestApp().run()