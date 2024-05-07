from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.app import App
from kivy.core.window import Window

class LoginPage(BoxLayout):
    """
    Classe que define a página de login.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # BoxLayout principal para centralizar verticalmente
        self.vertical_layout = BoxLayout(orientation="vertical", padding=20, spacing=10)
        self.add_widget(self.vertical_layout)
        
        self.username_box = BoxLayout(orientation="horizontal", size_hint_y=None, height=30)
        self.vertical_layout.add_widget(self.username_box)
        self.username_box.add_widget(Label(text="Username:", size_hint_x=None, width=100, halign="right"))
        self.username_input = TextInput(multiline=False)
        self.username_box.add_widget(self.username_input)
        
        self.password_box = BoxLayout(orientation="horizontal", size_hint_y=None, height=30)
        self.vertical_layout.add_widget(self.password_box)
        self.password_box.add_widget(Label(text="Password:", size_hint_x=None, width=100, halign="right"))
        self.password_input = TextInput(multiline=False, password=True)
        self.password_box.add_widget(self.password_input)
        
        self.login_button = Button(text="Login", size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5})
        self.login_button.bind(on_press=self.login)
        self.vertical_layout.add_widget(self.login_button)
        
    def login(self, instance):
        """
        Método chamado quando o botão de login é pressionado.
        """
        username = self.username_input.text
        password = self.password_input.text
        # Aqui você pode adicionar sua lógica de login, como verificar as credenciais
        print("Usuário:", username)
        print("Senha:", password)
        # Por simplicidade, vamos apenas imprimir o nome de usuário e a senha por enquanto

class MyApp(App):
    def build(self):
        # Definir largura e altura da janela
        self.title = "Login"
        Window.size = (400, 170)
        return LoginPage()

if __name__ == "__main__":
    MyApp().run()

