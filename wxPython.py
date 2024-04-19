import wx
import random

class Interfaz(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Interfaz')
        panel = wx.Panel(self)

        self.label = wx.StaticText(panel, label='Ingrese su nombre:')
        self.input = wx.TextCtrl(panel, size=(200, 25))
        self.boton_enviar = wx.Button(panel, label='Enviar')
        self.boton_color = wx.Button(panel, label='Cambiar color')

        font = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.label.SetFont(font)
        self.input.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.boton_enviar.SetBackgroundColour(wx.Colour(0, 150, 0))
        self.boton_enviar.SetForegroundColour(wx.WHITE)
        self.boton_color.SetBackgroundColour(wx.Colour(0, 0, 150))
        self.boton_color.SetForegroundColour(wx.WHITE)

        # Crear el sizer vertical y agregar los elementos con estilos
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.label, 0, wx.ALL | wx.CENTER, 10)
        sizer.Add(self.input, 0, wx.ALL | wx.CENTER, 10)
        sizer.Add(self.boton_enviar, 0, wx.ALL | wx.CENTER, 10)
        sizer.Add(self.boton_color, 0, wx.ALL | wx.CENTER, 10)

        panel.SetSizer(sizer)

        # Conectar las señales de los botones con los eventos
        self.boton_enviar.Bind(wx.EVT_BUTTON, self.on_enviar)
        self.boton_color.Bind(wx.EVT_BUTTON, self.on_cambiar_color)

        self.SetBackgroundColour(wx.Colour(200, 200, 200))
        self.SetSize((300, 250))
        self.Center()

    def on_enviar(self, event):
        nombre = self.input.GetValue()
        wx.MessageBox(f'¡Hola, {nombre}!', 'Saludo', wx.OK | wx.ICON_INFORMATION)

    def on_cambiar_color(self, event):
        colores = [
            wx.Colour(255, 200, 200),  
            wx.Colour(200, 255, 200), 
            wx.Colour(200, 200, 255),
            wx.Colour(255, 255, 200), 
            wx.Colour(255, 200, 255),  
            wx.Colour(200, 255, 255)  
        ]
        color = random.choice(colores)
        self.SetBackgroundColour(color)
        self.Refresh()

if __name__ == '__main__':
    app = wx.App()
    ventana = Interfaz()
    ventana.Show()
    app.MainLoop()