"""
This module is used to create animations for the game.

[x] Animations can either repeat or hold.
"""
import glob
import arcade


def load_texture_pair(filename: str):
    """
    Load a texture pair, with the second being a mirror image.
    """
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, mirrored=True)
    ]


class Animation:
    """
    This class represents a sequence of frames that can be used as an animation.
    """

    def __init__(self, dirpath: str, tick_count: int, repeats: bool):
        """
        Initialize the animation with the given directory path, tick count, and repeat flag.
        """
        self.frame_paths = sorted(glob.glob(dirpath + "/*.png"))
        if not self.frame_paths:
            raise RuntimeError(f"No frames in {dirpath}")
        self.textures = [load_texture_pair(x) for x in self.frame_paths]
        self.frame_count = len(self.frame_paths)
        self.tick_count = tick_count
        self.step, self.remainder = divmod(self.tick_count, self.frame_count)
        self.check = self.frame_count * self.step
        self.repeats = repeats

    def get_frame(self, index_count: int, direction: int = 0):
        """
        Get the frame at the given index count and direction.
        """
        if index_count > self.check-1 and not self.repeats:
            return self.textures[-1][direction]
        idx = (index_count // self.step) % self.frame_count
        return self.textures[idx][direction]
