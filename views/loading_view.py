"""
This file contains the LoadingView class, which is a subclass of arcade.View.
"""
import arcade
from pyglet.window import Window

from constants import SCREEN_WIDTH, Y_BASELINE, BOX_HEIGHT, BOX_WIDTH
from models import Player
from .fight_view import FightView


class LoadingView(arcade.View):
    """
    This class represents the loading screen that the player sees when the game is loading.
    """

    def __init__(self, window: Window):
        """
        Initialize the loading screen with the given window.
        """
        super().__init__()
        self.window = window
        self.idx = 0
        arcade.set_background_color(arcade.color.BLACK)
        self.tick_idx = 0
        self.drawn = False

    def on_draw(self):
        """
        Draw the game state.
        """
        arcade.start_render()
        arcade.draw_text(
            "Loading Characters...",
            self.window.width/2, self.window.height/2,
            arcade.color.WHITE, font_size=50, anchor_x="center"
        )
        arcade.draw_text(
            "(May take a moment)",
            self.window.width/2, self.window.height/2 - 30,
            arcade.color.WHITE, font_size=30, anchor_x="center"
        )
        self.tick_idx += 1
        self.drawn = True

    def on_update(self, delta_time):
        """
        Update the game state.
        """
        if self.drawn:
            player1 = Player(
                int(1/8 * SCREEN_WIDTH), Y_BASELINE,
                BOX_WIDTH, BOX_HEIGHT, 0,
                character='nate'
            )
            player2 = Player(
                int(7/8 * SCREEN_WIDTH), Y_BASELINE,
                BOX_WIDTH, BOX_HEIGHT, 1, character='nate'
            )
            fight_view = FightView(self.window, player1, player2)
            self.window.show_view(fight_view)
