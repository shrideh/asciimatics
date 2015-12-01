from asciimatics.effects import Julia
from asciimatics.widgets import Frame, TextBox, Layout, Label
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
import sys


class DemoFrame(Frame):
    def __init__(self, screen):
        super(DemoFrame, self).__init__(screen)
        layout = Layout([2, 6, 2])
        self.add_layout(layout)
        layout.add_widget(TextBox("Hello world!", 5, name="My First Box"), 1)
        layout.add_widget(Label("Some label"), 1)
        layout.add_widget(TextBox("Hello world!", 2, name="Second"), 1)
        layout.add_widget(TextBox("Hello world!", 10, name="Third"), 0)
        layout.add_widget(TextBox("Hello world!", 1, name="Fourth"), 2)
        layout2 = Layout([100])
        self.add_layout(layout2)
        layout2.add_widget(TextBox("Hello world!", 6, name="Big one"))
        layout3 = Layout([1, 1, 1])
        self.add_layout(layout3)
        layout3.add_widget(TextBox("Hello world!", 1, name="A"), 0)
        layout3.add_widget(TextBox("Hello world!", 2, name="B"), 1)
        layout3.add_widget(TextBox("Hello world!", 3, name="C"), 2)
        self.fix()

def demo(screen):
    scenes = []
    effects = [
        Julia(screen),
        DemoFrame(screen)
    ]
    scenes.append(Scene(effects, -1))

    screen.play(scenes, stop_on_resize=True)

while True:
    try:
        Screen.wrapper(demo)
        sys.exit(0)
    except ResizeScreenError:
        pass
