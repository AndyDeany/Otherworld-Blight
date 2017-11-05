"""Module containing the Intro view for playing out the intro sequence."""
from pygametemplate import View, load_font


class IntroView(View):

    background_colour = (255, 255, 255)
    text_colour = (0, 0, 0)
    font = load_font("chewy", 80)
    intro_text = "Leviathan Operations"

    def load(self):
        width, height = self.font.size(self.intro_text)
        self.coords = ((self.game.width - width)//2, (self.game.height - height)//2)

    def unload(self):
        pass

    def logic(self):
        CONTINUE_BUTTONS = ("escape", " ", "enter", "numpadenter")
        if any(self.game.input.buttons.pressed for key in CONTINUE_BUTTONS):
            self.game.set_view("MainMenu")

        current_length = self.game.frame//10
        if current_length > len(self.intro_text):
            self.game.set_view("MainMenu")
            return

        current_text = self.intro_text[:current_length]
        self.text = self.font.render(current_text, True, self.text_colour)

    def draw(self):
        self.game.screen.fill(self.background_colour)
        self.game.screen.blit(self.text, self.coords)
