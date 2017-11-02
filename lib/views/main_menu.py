"""Module containing the MainMenu view for representing the main menu."""
from pygametemplate import View, Image

from lib.views import SavesMenu, OptionsMenu, Controls


class MainMenu(View):

    background = Image("menus/main/background.png")
    title = Image("menus/main/title.png")

    PLAY = Image("menus/main/play.png")
    OPTIONS = Image("menus/main/options.png")
    CONTROLS = Image("menus/main/controls.png")
    EXIT = Image("menus/main/exit.png")
    items = [PLAY, OPTIONS, CONTROLS, EXIT]

    images = [background, title] + items

    def load(self):
        self.selection_index = 0
        for image in self.images:
            image.load()

    def unload(self):
        for image in self.images:
            image.unload()

    def logic(self):
        if any(self.game.input.buttons[key].pressed for key in ("up", "w")):
            self.selection_index -= 1
            if self.selection_index == -1:
                self.selection_index += len(self.items)

        if any(self.game.input.buttons[key].pressed for key in ("down", "s")):
            self.selection_index += 1
            if self.selection_index == len(self.items):
                self.selection_index = 0

        CONFIRM_BUTTONS = ("leftmouse", " ", "enter", "numpadenter")
        if any(self.game.input.buttons[button].pressed for button in CONFIRM_BUTTONS):
            selection = self.items[self.selection_index]
            if selection == self.PLAY:
                self.game.set_view(SavesMenu)
            elif selection == self.OPTIONS:
                self.game.set_view(OptionsMenu)
            elif selection == self.CONTROLS:
                self.game.set_view(Controls)
            elif selection == self.EXIT:
                self.game.running = False   # TODO: Use upcoming self.game.quit() method

    def draw(self):
        self.background.display(self.game.screen, (0, 0))
        self.title.display(self.game.screen, (0, 0))
        self.items[self.selection_index].display(self.game.screen, (0, 0))
