from Tool import *


class Rake(Tool):
    tool_type = ToolType.RAKE

    def __init__(self, weight, work):
        self.weight = weight
        self.work = work
