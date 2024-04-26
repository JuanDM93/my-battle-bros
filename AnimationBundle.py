"""
This file is responsible for creating the animation bundle for each character.

character
    stance
        activity
"""
import os
import pickle
import glob
import random

from Animation import Animation
from constants import (
    SPRITES_ROOT, SPRITES_CACHE_DIR,
    ATTACK_TIME, BLOCK_INIT_TIME, HIT_RECOVER_TIME,
    IDLE_ANIMATION_TIME, MOVEMENT_ANIMATION_TIME,
    WIN_TIME, LOSE_TIME, START_TIME,
)

STANCES = {
    "high",
    "medium",
    "low"
}
ACTIVITIES = {
    "attack",
    "block",
    "hit",
    "idle",
    "movement"
}

ACTIVITY_PARAMS = {
    "attack": (ATTACK_TIME, False),
    "block": (BLOCK_INIT_TIME, False),
    "hit": (HIT_RECOVER_TIME, False),
    "idle": (IDLE_ANIMATION_TIME, True),
    "movement": (MOVEMENT_ANIMATION_TIME, True),
    'win': (WIN_TIME, False),
    'lose': (LOSE_TIME, False),
    'start': (START_TIME, False)
}


def build_animations_registry(character):
    """
    Build the animations registry for the given character.
    """
    character_registry_cache_path = os.path.join(SPRITES_CACHE_DIR, character)
    if os.path.exists(character_registry_cache_path):
        with open(character_registry_cache_path, 'rb') as fin:
            return pickle.load(fin)
    character_dir = SPRITES_ROOT + "/" + character
    animations_registry = {}
    # Combations
    for stance in STANCES:
        for activity in ACTIVITIES:
            key = (stance, activity)
            animations_registry[key] = ActivityAnimationBundle(
                character_dir + '/' + stance, activity)

    # Specials
    animations_registry['win'] = ActivityAnimationBundle(
        character_dir + '/end', 'win')
    animations_registry['lose'] = ActivityAnimationBundle(
        character_dir+'/end', 'lose')
    animations_registry['start'] = ActivityAnimationBundle(
        character_dir, 'start')
    with open(character_registry_cache_path, 'wb') as fout:
        pickle.dump(animations_registry, fout)
    return animations_registry


class ActivityAnimationBundle:
    """
    This class represents a bundle of animations for a given activity.
    """

    def __init__(self, stance_path, action):
        """
        Initialize the animation bundle with the given stance path and action.
        """
        print(stance_path)
        self.path = stance_path + "/" + action
        self.sub_dirs = glob.glob(self.path + '/*')
        self.animations = [Animation(
            x, ACTIVITY_PARAMS[action][0], ACTIVITY_PARAMS[action][1]) for x in self.sub_dirs]

    def random_animation(self):
        """
        Get a random animation from the bundle.
        """
        return random.choice(self.animations)
