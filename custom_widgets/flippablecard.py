from kivymd.app import MDApp
from kivymd.uix.carousel import MDCarousel
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.properties import NumericProperty


class FlippableCard(ButtonBehavior, FloatLayout):
    scale_x = NumericProperty(1)

    def __init__(self, front_image, title, meaning, **kwargs):
        super().__init__(**kwargs)
        self.front_image = front_image
        self.title = title
        self.meaning = meaning
        self.flipped = False

        self.build_front()

    # -------------------------
    # FRONT
    # -------------------------
    def build_front(self):
        from kivymd.uix.fitimage import FitImage

        self.ids.card.clear_widgets()

        img = FitImage(
            source=self.front_image,
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

        self.ids.card.clear_widgets()

        layout = MDBoxLayout(
            orientation='vertical',
            spacing="10dp"
        )

        title = MDLabel(
            text=self.title,
            halign="center",
            theme_text_color="Primary",
            font_style="H5",
            size_hint_y=0.2
        )

        meaning = MDLabel(
            text=self.meaning,
            halign="center",
            theme_text_color="Secondary"
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
    def on_press(self):
        self.flip()

    def flip(self):
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

        Animation(
            scale_x=1,
            duration=0.2,
            t='in_quad'
        ).start(self)

    # -------------------------
    # POPUP (KivyMD style)
    # -------------------------
    def show_more(self, *args):
        from kivymd.uix.dialog import MDDialog
        from kivymd.uix.button import MDFlatButton

        self.dialog = MDDialog(
            title=self.title,
            text=f"Full meaning of {self.title}...\n\n(Add your deep interpretation here.)",
            buttons=[
                MDFlatButton(
                    text="CLOSE",
                    on_release=lambda x: self.dialog.dismiss()
                )
            ],
        )
        self.dialog.open()


# -------------------------
# MAIN APP
# -------------------------
class TarotApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Dark"

        carousel = Carousel(direction='right')

        cards = [
            ("fool.png", "The Fool", "New beginnings, innocence, spontaneity."),
            ("magician.png", "The Magician", "Manifestation, power, inspired action."),
            ("high_priestess.png", "The High Priestess", "Intuition, mystery, inner knowing."),
        ]

        for img, title, meaning in cards:
            card = FlippableCard(
                front_image=img,
                title=title,
                meaning=meaning
            )
            carousel.add_widget(card)
            
        return carousel


1