"""
This module contains the FightView class, which is responsible for rendering the fight scene.
"""
import os
import glob
import random

import arcade
from pyglet.window import Window

from models import Player
from constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_IMG_ROOT,
    MUSIC_ROOT, COUNTDOWN_FROM, TICKS_PER_COUNTDOWN,
    FIGHT_MSG, STRIKE_DISTANCE, ATTACK_OFFSET, ATTACK_FUDGE,
)


class FightView(arcade.View):
    """
    This class is responsible for rendering the fight scene.
    """

    def __init__(
        self,
        window: Window,
        player1: Player, player2: Player
    ):
        """
        Initialize the fight scene with the given window and players.
        """
        super().__init__()

        self.window = window
        self.window.set_mouse_visible(False)

        self.player1 = player1
        self.player2 = player2

        # endgame
        self.winner: Player = None

        # background images
        bg_images = glob.glob(os.path.join(BACKGROUND_IMG_ROOT, "*.png"))
        bg_image = random.choice(bg_images)
        self.background_texture = arcade.load_texture(bg_image)

        # background music
        self.enable_bg_music = True
        if self.enable_bg_music:
            songs = glob.glob(os.path.join(MUSIC_ROOT, "*.wav"))
            bg_song = random.choice(songs)
            self.background_music = arcade.load_sound(bg_song)
            arcade.play_sound(self.background_music)

        # Initial Countdown
        self.countdown_counter = (COUNTDOWN_FROM + 1) * TICKS_PER_COUNTDOWN
        self.countdown_values = range(1, COUNTDOWN_FROM+1)

    def on_key_press(self, symbol, modifiers):
        """
        Handle key press events.
        """
        if not self.winner and not self.countdown_counter:
            self.player1.on_keypress(symbol, modifiers)
            self.player2.on_keypress(symbol, modifiers)

    def on_key_release(self, key, modifiers):
        """
        Handle key release events.
        """
        if not self.winner and not self.countdown_counter:
            self.player1.on_key_release(key, modifiers)
            self.player2.on_key_release(key, modifiers)

    def _update_winner(self):
        """
        Update the winner of the game.
        """
        if self.player1.health < 1:
            self.winner = self.player2
        if self.player2.health < 1:
            self.winner = self.player1

        if self.winner and self.enable_bg_music:
            self.player1.game_over = True
            self.player2.game_over = True

    def on_update(self, delta_time):
        """
        Update the game state.
        """
        if self.countdown_counter:
            self.countdown_counter -= 1
            if self.countdown_counter == TICKS_PER_COUNTDOWN:
                # set the players so they're ready to go
                self.player1.state = ('medium', 'idle')
                self.player2.state = ('medium', 'idle')
        else:
            self._update_winner()
            if self.player1.center_x < self.player2.center_x:
                win_dir = 0
            else:
                win_dir = 1
            self.player1.update_initial(win_dir)
            self.player2.update_initial(win_dir)
            # handle hits
            if abs(self.player1.center_x - self.player2.center_x) < STRIKE_DISTANCE:
                if ATTACK_OFFSET < self.player1.attack_counter <= ATTACK_OFFSET + ATTACK_FUDGE:
                    self.player2.hit_update(self.player1)
                if ATTACK_OFFSET < self.player2.attack_counter <= ATTACK_OFFSET + ATTACK_FUDGE:
                    self.player1.hit_update(self.player2)

    def on_draw(self):
        """
        Draw the game state.
        """
        arcade.start_render()

        # Draw background
        arcade.draw_texture_rectangle(
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
            SCREEN_WIDTH, SCREEN_HEIGHT, self.background_texture
        )
        # Draw players
        self.player1.draw()
        self.player2.draw()

        # Draw countdown timer
        if self.countdown_counter > TICKS_PER_COUNTDOWN:
            arcade.draw_text(
                f"{self.countdown_values[
                    (self.countdown_counter-TICKS_PER_COUNTDOWN-1) // TICKS_PER_COUNTDOWN
                ]}",
                SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.RED,
                font_size=120, anchor_x="center", font_name="Utopia", bold=True
            )
        # Draw "Fight" message
        elif self.countdown_counter:
            arcade.draw_text(
                FIGHT_MSG, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.RED,
                font_size=120, anchor_x="center", font_name="Utopia", bold=True
            )
        # Draw "Winner message
        elif self.winner:
            arcade.draw_text(
                f"Player {self.winner.player_idx + 1} WINS!!",
                SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.RED,
                font_size=60, anchor_x="center", font_name="Utopia"
            )
