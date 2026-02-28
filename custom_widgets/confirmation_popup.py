from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import StringProperty, ObjectProperty
from kivy.animation import Animation


class ConfirmDialog(Popup):
    text = StringProperty("Are you sure?")
    on_confirm = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.size_hint = (0.8, 0.4)
        self.title = "Confirm"
        self.opacity = 0  # start invisible

        layout = BoxLayout(orientation="vertical", spacing=20, padding=20)

        message = Label(
        text=self.text,
        halign="center",
        valign="middle"
        )
    
    # Force wrapping inside the popup width
        message.bind(
            size=lambda instance, value: setattr(instance, 'text_size', (instance.width, None))
        )

        button_layout = BoxLayout(spacing=20, size_hint_y=None, height=50)

        yes_button = Button(text="Yes")
        no_button = Button(text="No")

        yes_button.bind(on_release=self._yes_pressed)
        no_button.bind(on_release=self.fade_dismiss)

        button_layout.add_widget(yes_button)
        button_layout.add_widget(no_button)

        layout.add_widget(message)
        layout.add_widget(button_layout)

        self.content = layout

    # Fade in
    def open(self, *args, **kwargs):
        super().open(*args, **kwargs)
        Animation(opacity=1, duration=0.3).start(self)

    # Fade out
    def fade_dismiss(self, *args):
        anim = Animation(opacity=0, duration=0.6)
        anim.bind(on_complete=lambda *x: self.dismiss)
        anim.start(self)

    def _yes_pressed(self, *args):
        if self.on_confirm:
            self.on_confirm()
        self.fade_dismiss()