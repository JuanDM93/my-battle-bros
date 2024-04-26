"""
This file contains all the constants used in the game.
"""
from enum import Enum
import os

# GAME SCREEN PARAMETERS
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "BROGAME"

# PLAYER PARAMETERS
BOX_WIDTH = SCREEN_WIDTH // 10
BOX_HEIGHT = SCREEN_HEIGHT // 1.5
MOVEMENT_SPEED = 8
STRIKE_DISTANCE = 150
HIT_DAMAGE = 10
JUMP_SPEED = 25
CHARACTER_SCALING = 1
GRAV_CONSTANT = 9.8/9
Y_BASELINE = 200
JUMP_FUDGE = 30  # amount above baseline where we allow the user to "jump" again
KNOCKBACK_DISTANCE = 100

# HEALTHBAR
HEALTHBAR_Y_OFFSET = 40
HEALTHBAR_X_OFFSET = 10
HEALTHBAR_HEIGHT = 40
HEALTHBAR_PADDING = 8
HEALTHBAR_WIDTH = 300

# TIMING CONSTANTS -- all values are in game ticks.
BLOCK_INIT_TIME = 20  # ticks until block active
BLOCK_ACTIVE_TIME = 50  # ticks until block wears off
BLOCK_TOTAL_TIME = BLOCK_INIT_TIME + BLOCK_ACTIVE_TIME
ATTACK_TIME = 30
ATTACK_OFFSET = 5
ATTACK_FUDGE = 1
HIT_RECOVER_TIME = 20  # in game steps
IDLE_ANIMATION_TIME = 100
MOVEMENT_ANIMATION_TIME = 100
START_TIME = 200
WIN_TIME = 200
LOSE_TIME = 100

# DIRECTORY PATHS
PROJECT_ROOT = os.path.dirname(__file__)
SPRITES_ROOT = os.path.join(PROJECT_ROOT, "sprites")
SOUND_ROOT = os.path.join(PROJECT_ROOT, "sounds")
MUSIC_ROOT = os.path.join(PROJECT_ROOT, "music")
BACKGROUND_IMG_ROOT = os.path.join(PROJECT_ROOT, "backgrounds")
SPRITES_CACHE_DIR = os.path.join(PROJECT_ROOT, '.sprites_cache')

if not os.path.exists(SPRITES_CACHE_DIR):
    os.mkdir(SPRITES_CACHE_DIR)


# COUNTDOWN TIMER
TICKS_PER_COUNTDOWN = 40
COUNTDOWN_FROM = 5
FIGHT_MSG = "FIGHT!"


class LevelStates(Enum):
    """
    Enum for the different states of the game
    """
    low = 0
    medium = 1
    # high is implicit, encoded


class EventStates(Enum):
    """
    Enum for the different states of the game
    """
    idle = 0
    blocking = 1
    attacking = 2
    hit = 3
