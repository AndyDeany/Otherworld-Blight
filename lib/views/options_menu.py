"""Module containing the OptionsMenu view for showing the options menu."""
from pygametemplate import View, Image


class OptionsMenu(View):

    background = Image("menus/background.png")
    headings = Image("menus/options/headings.png")
    resolution_images = [
        Image("menus/options/resolutions/{}.png".format(resolution)) for resolution in (
            "800x600",
            "1024x768",
            "1152x864",
            "1280x720", "1280x768", "1280x800", "1280x960", "1280x1024",
            "1366x768",
            "1600x900", "1600x1024",
            "1680x1050",
            "1920x1080",
        )
    ]

    def load(self):
        pass

    def unload(self):
        pass

    def logic(self):
        pass

    def draw(self):
        pass
