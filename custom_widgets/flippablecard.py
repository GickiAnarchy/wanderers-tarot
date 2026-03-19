from kivy.clock import Clock
from kivy.animation import Animation
from kivy.properties import NumericProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout


class FlippableCard(ButtonBehavior, FloatLayout):
    scale_x = NumericProperty(1)

    def __init__(self, riderCard, **kwargs):
        super().__init__(**kwargs)

        self.model_card = riderCard
        self.image = f"data/images/{self.model_card.image}"
        self.name = self.model_card.name

        self.flipped = False
        self.animating = False  # 🧠 prevents spam taps

        # ⏳ wait until KV is ready
        Clock.schedule_once(self._finish_init)

    def _finish_init(self, *args):
        self.build_front()

    # -------------------------
    # FRONT
    # -------------------------
    def build_front(self):
        from kivymd.uix.fitimage import FitImage

        if "card" not in self.ids:
            return

        self.ids.card.clear_widgets()

        img = FitImage(
            source=self.image,
            radius=[20]
        )

        self.ids.card.add_widget(img)

    # -------------------------
    # BACK
    # -------------------------
    def build_back(self):
        from kivymd.uix.label import MDLabel
        from kivymd.uix.button import MDRaisedButton
        from kivymd.uix.boxlayout import MDBoxLayout

        if "card" not in self.ids:
            return

        self.ids.card.clear_widgets()

        layout = MDBoxLayout(
            orientation='vertical',
            spacing="10dp",
            padding="10dp"
        )

        title = MDLabel(
            text=self.name,
            halign="center",
            font_style="H5",
            size_hint_y=0.2
        )

        meaning = MDLabel(
            text=f"Meaning of {self.name}...",
            halign="center"
        )

        btn = MDRaisedButton(
            text="Show More",
            pos_hint={"center_x": 0.5}
        )
        btn.bind(on_release=self.show_more)

        layout.add_widget(title)
        layout.add_widget(meaning)
        layout.add_widget(btn)

        self.ids.card.add_widget(layout)

    # -------------------------
    # FLIP
    # -------------------------
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.flip()
            return True  # 👈 consume the touch
    
        return super().on_touch_down(touch)
    
    
    def on_press(self):
        if self.animating:
            return
        self.flip()

    def flip(self):
        self.animating = True

        anim1 = Animation(
            scale_x=0,
            duration=0.2,
            t='out_quad'
        )

        anim1.bind(on_complete=self._swap_face)
        anim1.start(self)

    def _swap_face(self, *args):
        if self.flipped:
            self.build_front()
        else:
            self.build_back()

        self.flipped = not self.flipped

        anim2 = Animation(
            scale_x=1,
            duration=0.2,
            t='in_quad'
        )

        anim2.bind(on_complete=self._done_animating)
        anim2.start(self)

    def _done_animating(self, *args):
        self.animating = False

    # -------------------------
    # POPUP
    # -------------------------
    def show_more(self, *args):
        from kivymd.uix.dialog import MDDialog
        from kivymd.uix.button import MDFlatButton

        dialog = MDDialog(
            title=self.name,
            text=f"Full meaning of {self.name}...\n\n(Add your deep interpretation here.)",
            buttons=[
                MDFlatButton(
                    text="CLOSE",
                    on_release=lambda x: dialog.dismiss()
                )
            ],
        )
        dialog.open()