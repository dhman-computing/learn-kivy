from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


# Define the main application class
class CounterApp(App):
    def build(self):
        return MainBoxLayout()


# Define a custom BoxLayout class
class MainBoxLayout(BoxLayout):
    def change_text(self):
        self.ids.my_label.text = "Button Clicked!"


# Run the application
CounterApp().run()
