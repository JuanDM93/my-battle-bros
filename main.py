"""
Main file to run the game
"""
import arcade
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from views import IntroView


def main():
    """
    Main method to run the game
    """
    window = arcade.Window(
        title=SCREEN_TITLE,
        width=SCREEN_WIDTH, height=SCREEN_HEIGHT,
    )
    menu_view = IntroView(window)
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()
