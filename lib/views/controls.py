"""Module containing the Controls view for showing the controls."""
from pygametemplate import View, Image


class Controls(View):

    background = Image("menus/background.png")
    controls_image = Image("menus/controls.png")
    images = [background, controls_image]

    def load(self):
        for image in self.images:
            image.load()

    def unload(self):
        for image in self.images:
            image.unload()

    def logic(self):
        if any(self.game.input.buttons[key].pressed for key in ("escape", "backspace")):
            self.game.set_view("MainMenu")

    def draw(self):
        self.background.display(self.game.screen, (0, 0))
        self.controls_image.display(self.game.screen, (0, 0))
