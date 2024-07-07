from kivy.app import App
from kivy.uix.gridlayout import GridLayout


# Define the main application class
class CounterApp(App):
    def build(self):
        return MainGridLayout()


# Define a custom BoxLayout class
class MainGridLayout(GridLayout):
    cnt = 0

    def inc_count(self, cnt):
        self.ids.count.text = f"{cnt + 1}"

    def dec_count(self, cnt):
        self.ids.count.text = f"{cnt - 1}"


# Run the application
CounterApp().run()
