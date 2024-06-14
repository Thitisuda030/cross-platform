from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen

class Scr_home (Screen):
    pass

class Scr_register (Screen):
    pass


class Ui(ScreenManager):
    pass

class dltApp(App):
    def build(self):
        return Ui()
    
if __name__=="__main__":
    dltApp().run()