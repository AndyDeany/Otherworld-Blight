from lib.otherworld_blight import OtherworldBlight
from lib.views import IntroView

caption = "Otherworld Blight v1.0.0"

game = OtherworldBlight(IntroView, caption=caption, icon="game_icon.png")
game.run()
