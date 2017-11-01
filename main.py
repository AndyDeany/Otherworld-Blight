from lib.otherworld_blight import OtherworldBlight
from lib.views import IntroView


RESOLUTION = (1920, 1080)
MODE = "fullscreen"
CAPTION = "Otherworld Blight v1.0.0"


if __name__ == "__main__":
    game = OtherworldBlight(IntroView, RESOLUTION, MODE,
                            caption=CAPTION, icon="game_icon.png")
    game.run()
