'''
Code with Jonathan 08/05/24
'''
# from kivy.app import App
# from kivy.uix.widget import Widget


# class MainWidget(Widget):
#     pass

# class TheLabApp(App):
#     pass

# app = TheLabApp()

# app.run()
# Arquivo: main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MeuApp(BoxLayout):
    def btn_click(self):
        print("Botão clicado!")

class MyApp(App):
    def build(self):
        return MeuApp()

if __name__ == '__main__':
    MyApp().run()
