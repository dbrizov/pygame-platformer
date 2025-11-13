import pygame
import pathlib
from engine.color import Color
from engine.graphics import Graphics


class Assets:
    @staticmethod
    def load_image(path: str | pathlib.Path, colorkey: Color | None = None) -> pygame.Surface:
        """
        Load an image as a Pygame Surface with fast blitting and optional transparency.

        Args:
            path: File path to the image.
            colorkey: Optional color to treat as transparent in addition to any alpha channel.

        Returns:
            pygame.Surface ready for blitting
        """
        image = pygame.image.load(path)

        if image.get_alpha() is not None:
            image = image.convert_alpha()  # Keep alpha, convert to display format
        else:
            image = image.convert()  # No alpha: convert to display format for speed

        if colorkey is not None:
            image.set_colorkey(colorkey)  # Set colorkey for transparency

        if Graphics.scale != 1.0:
            image = pygame.transform.scale_by(image, Graphics.scale)

        return image
