from enum import Enum


class ToolType(Enum):
    RAKE = 1
    SHOVEL = 2
    SECATEUR = 3


class Work(Enum):
    TAKE_LEAVES = 1
    DIG_GROUND = 2
    CUT_BRANCHES = 3


class Tool:
    price = 0.0
    weight = 0.0
    work = None
    tool_type = None

    def __str__(self):
        return self.work.name + ' ' + self.tool_type.name