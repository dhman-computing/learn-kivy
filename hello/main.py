# import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


# Define the main application class
class HelloApp(App):
    def build(self):
        # The root widget is automatically loaded from the .kv file
        return MyBoxLayout()


# Define a custom BoxLayout class
class MyBoxLayout(BoxLayout):
    pass


# Run the application
if __name__ == "__main__":
    HelloApp().run()
