from pydoc import text
from unittest.util import _MIN_COMMON_LEN

from kivy.clock import Clock
from kivy.animation import Animation
from kivy.properties import NumericProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.card import MDCard



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
        #self.build_back()

    # -------------------------
    # FRONT
    # -------------------------
    def build_front(self):
        from kivymd.uix.fitimage import FitImage

        if "card" not in self.ids:
            return

        self.ids.card.clear_widgets()

        container = MDBoxLayout(
            size_hint=(None, None),
            size=("250dp", "425dp"),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )

        img = FitImage(
            source=self.image,
            radius=[20],
            
        )

        container.add_widget(img)

        self.ids.card.add_widget(container)

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

        meanings_scroll = MDScrollView(
            id = "meanings_scroll",
            do_scroll_x=False,
            do_scroll_y=True,
        )

        mean_box = MDBoxLayout(
            orientation='vertical',
            size_hint_y=None,
            padding="5dp"
        )
        mean_box.bind(minimum_height=mean_box.setter('height'))

        meaning = MDLabel(
            text=f"Meaning:\n{self.model_card.get_meanings()}",
            halign="left",
            valign="top",
            size_hint_y=None
            )
        
        """
        meaning.height = meaning.texture_size[1]
        meaning.text_size = meaning.width, None
        """
            
        meaning.bind(width=lambda *x: setattr(meaning, "text_size", (meaning.width, None)))
        meaning.bind(texture_size=lambda *x: setattr(meaning, "height", meaning.texture_size[1]))

        mean_box.add_widget(meaning)
        meanings_scroll.add_widget(mean_box)

        btn = MDRaisedButton(
            text="Show More",
            pos_hint={"center_x": 0.5}
        )
        btn.bind(on_release=self.show_more)

        layout.add_widget(title)
        layout.add_widget(meanings_scroll)
        layout.add_widget(btn)

        self.ids.card.add_widget(layout)

    # -------------------------
    # FLIP
    # -------------------------
    def on_press(self):
        # If the scrollview exists and the touch started inside it, ignore flip
        if "meanings_scroll" in self.ids:
            sv = self.ids.meanings_scroll
            if sv.collide_point(*self.last_touch_pos):
                return

        if not self.animating:
            self.flip()

    def on_touch_down(self, touch):
        # Save touch position so on_press can check it
        self.last_touch_pos = touch.pos
        return super().on_touch_down(touch)

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