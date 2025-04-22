from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.metrics import sp, dp
from kivy.core.window import Window
import time

class CalculadoraLeite(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=dp(20), spacing=dp(10), **kwargs)

        self.add_widget(Label(
            text="Bem-vinda a Calculadora de Leite Materno!",
            font_size=sp(22),
            halign="center",
            valign="middle",
            size_hint_y=None,
            height=dp(50)
        ))

        self.authors_label = Label(
            text="Este aplicativo foi escrito por Bruno P. S., Gabriel A. da S., Jefferson de L. P., e Luiz R. M.",
            font_size=sp(14),
            halign="center",
            valign="middle",
            size_hint_y=None,
            height=dp(40)
        )
        self.authors_label.bind(width=lambda instance, value: setattr(instance, 'text_size', (value - dp(20), None)))
        self.add_widget(self.authors_label)

        self.add_widget(Label(
            text="Digite o peso do bebê em kg (ex: 3.2):",
            font_size=sp(18),
            size_hint_y=None,
            height=dp(30)
        ))

        self.weight_input = TextInput(
            multiline=False,
            input_filter='float',
            font_size=sp(18),
            size_hint_y=None,
            height=dp(50)
        )
        self.add_widget(self.weight_input)

        self.result_label = Label(
            text="",
            font_size=sp(16),
            halign="left",
            valign="top",
            text_size=(self.width, None),
            size_hint_y=None,
            height=dp(100)
        )
        self.result_label.bind(width=self.update_text_wrap)
        self.add_widget(self.result_label)

        self.time_label = Label(
            text="",
            font_size=sp(14),
            size_hint_y=None,
            height=dp(30)
        )
        self.add_widget(self.time_label)

        self.info_label = Label(
            text="",
            font_size=sp(12),
            size_hint_y=None,
            height=dp(25)
        )
        self.add_widget(self.info_label)

        self.calc_button = Button(
            text="Calcular",
            font_size=sp(18),
            size_hint_y=None,
            height=dp(50)
        )
        self.calc_button.bind(on_press=self.calculate)
        self.add_widget(self.calc_button)

        self.check_orientation()
        Window.bind(on_resize=self.on_window_resize)

    def update_text_wrap(self, instance, width):
        instance.text_size = (width - dp(20), None)

    def mostrar_hora_e_data(self):
        current_time = time.strftime("%H:%M:%S")
        current_date = time.strftime("%Y-%m-%d")
        return f"{current_time} on {current_date}"

    def calcular_leite_e_periodo_alimentacao(self, peso):
        aviso = "Por favor consultar com a sua pediatria para as melhores necessidades nutricionais para o seu bebê."
        if 0.1 <= peso <= 1.9:
            leite, periodo = 25, 3
        elif 2.0 <= peso <= 2.5:
            leite, periodo = 50, 4
        elif 2.6 <= peso <= 5.0:
            leite, periodo = 70, 5
        elif 5.1 <= peso <= 10.3:
            leite, periodo = 90, 6
        else:
            return "Peso fora do intervalo para bebês recém-nascidos."

        result = f"Para um bebê que pesa {peso} kg, ele pode tomar {leite} ml de leite a cada {periodo} horas."

        if peso < 2.5 or peso >= 4.5:
            result += f"\n\n{aviso}"

        return result

    def calculate(self, instance):
        try:
            peso = float(self.weight_input.text)
            result = self.calcular_leite_e_periodo_alimentacao(peso)
        except ValueError:
            result = "Por favor digite um número válido para o peso."

        self.result_label.text = result
        self.time_label.text = "Horário da verificação: " + self.mostrar_hora_e_data()

    def on_window_resize(self, window, width, height):
        self.check_orientation()

    def check_orientation(self):
        width, height = Window.size
        orientation = "paisagem" if width > height else "retrato"
        is_tablet = width >= dp(600)

        message = f"[Modo: {orientation}]"
        if is_tablet:
            message += " - Dispositivo com tela ampla detectado."

        self.info_label.text = message

class MPVCalculadoraLeiteMaterno(App):
    def build(self):
        return CalculadoraLeite()

if __name__ == '__main__':
    MPVCalculadoraLeiteMaterno().run()