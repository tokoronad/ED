import arcade
from menu import MainMenuView

SCREEN_WIDTH = 1980
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "Эволюционный защитник"


def main():
    window = arcade.Window(
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
        SCREEN_TITLE,
        fullscreen=True
    )
    window.show_view(MainMenuView())
    arcade.run()


if __name__ == "__main__":
    main()
