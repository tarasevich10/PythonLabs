from Tool import *


class Shovel(Tool):
    tool_type = ToolType.SHOVEL

    def __init__(self, weight, work):
        self.weight = weight
        self.work = work
