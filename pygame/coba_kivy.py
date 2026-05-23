import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class CounterApp(App):

    def build(self):
        self.count = 0

        layout = BoxLayout(orientation='vertical')

        self.label = Label(text=str(self.count), font_size=50)

        button = Button(text="Tambah", font_size=30)
        button.bind(on_press=self.increment)

        layout.add_widget(self.label)
        layout.add_widget(button)

        return layout

    def increment(self, instance):
        self.count += 1
        self.label.text = str(self.count)

if __name__ == "__main__":
    CounterApp().run()