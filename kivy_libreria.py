from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import random

class Interfaz(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=150, padding=100)

        label = Label(text='Ingresar el nombre:')
        layout.add_widget(label)

        self.nombre_input = TextInput(multiline=False, size_hint=(1, None), height=40)
        layout.add_widget(self.nombre_input)

        button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1.5, None), height=50)

        enviar_button = Button(text='Enviar', on_press=self.mostrar_saludo, size_hint=(1, 1), size=(120, 50))
        button_layout.add_widget(enviar_button)

        self.color_button = Button(text='Cambiar color', on_press=self.cambiar_color_texto, size_hint=(1, 1), size=(120, 50))
        button_layout.add_widget(self.color_button)

        button_layout.add_widget(Label(size_hint=(1, 1)))

        layout.add_widget(button_layout)

        self.colores = [(1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1), (1, 1, 0, 1), (1, 0, 1, 1), (0, 1, 1, 1)]

        return layout

    def mostrar_saludo(self, instance):
        nombre = self.nombre_input.text
        popup = Popup(title='Saludo',
                      content=Label(text=f'¡Hola, {nombre}!'),
                      size_hint=(None, None), size=(200, 200))
        popup.open()

    def cambiar_color_texto(self, instance):
        color = random.choice(self.colores)
        self.color_button.color = color

if __name__ == '__main__':
    Interfaz().run()