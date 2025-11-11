import pathlib
from configparser import ConfigParser


CURRENT_DIRECTORY = pathlib.Path(__file__).resolve().parent
CONFIG_FILE_NAME = "engine.ini"
CONFIG_FILE_PATH = CURRENT_DIRECTORY.joinpath(CONFIG_FILE_NAME)

# Config sections
SECTION_GRAPHICS = "graphics"
SECTION_PHYSICS = "physics"

# Graphics keys
KEY_SCREEN_WIDTH = "screen_width"
KEY_SCREEN_HEIGHT = "screen_height"
KEY_TARGET_FPS = "target_fps"
KEY_GRAPHICS_SCALE = "graphics_scale"

# Physics keys
KEY_PHYSICS_FPS = "physics_fps"
KEY_PHYSICS_INTERPOLATION = "physics_interpolation"


class EngineConfig:
    # Graphics
    SCREEN_WIDTH: int
    SCREEN_HEIGHT: int
    TARGET_FPS: int
    GRAPHICS_SCALE: float

    # Physics
    PHYSICS_FPS: int
    PHYSICS_DELTA_TIME: float
    PHYSICS_INTERPOLATION: bool

    @staticmethod
    def init():
        config = ConfigParser(allow_no_value=True)
        config.read(CONFIG_FILE_PATH)

        # Graphics
        EngineConfig.SCREEN_WIDTH = config.getint(SECTION_GRAPHICS, KEY_SCREEN_WIDTH)
        EngineConfig.SCREEN_HEIGHT = config.getint(SECTION_GRAPHICS, KEY_SCREEN_HEIGHT)
        EngineConfig.TARGET_FPS = config.getint(SECTION_GRAPHICS, KEY_TARGET_FPS)
        EngineConfig.GRAPHICS_SCALE = config.getfloat(SECTION_GRAPHICS, KEY_GRAPHICS_SCALE)

        # Physics
        EngineConfig.PHYSICS_FPS = config.getint(SECTION_PHYSICS, KEY_PHYSICS_FPS)
        EngineConfig.PHYSICS_DELTA_TIME = 1.0 / EngineConfig.PHYSICS_FPS
        EngineConfig.PHYSICS_INTERPOLATION = config.getboolean(SECTION_PHYSICS, KEY_PHYSICS_INTERPOLATION)
