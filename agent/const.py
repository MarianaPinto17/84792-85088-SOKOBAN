from enum import IntEnum,Enum

class Direction(Enum):
    UP = "w"
    LEFT = "a"
    DOWN = "s"
    RIGHT = "d"

StringToDir = {
    "w": Direction.UP,
    "a": Direction.LEFT,
    "s": Direction.DOWN,
    "d": Direction.RIGHT
}