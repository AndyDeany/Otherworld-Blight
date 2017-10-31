"""Module containing the Intro view for playing out the intro sequence."""
import pygame
from pygametemplate import View

from lib.views import MainMenu


class IntroView(View):

    def load(self):
        # TODO: Use upcoming pygametemplate.load_video() method
        self.intro_video = pygame._movie.Movie("assets/videos/intro.mpg")
        self.intro_video.set_display(self.game.screen)
        self.intro_video.play()

    def unload(self):
        self.intro_video = None

    def logic(self):
        if not self.intro_video.get_busy():  # Intro has finished
            self.game.switch_view(MainMenu)

        for key in ("escape", "space", "enter", "numpadenter"):
            if self.game.input.buttons[key].pressed:
                self.game.switch_view(MainMenu)

    def draw(self):
        pass
