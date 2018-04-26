from Tool import *


class Secateur(Tool):
    tool_type = ToolType.SECATEUR

    def __init__(self, price, work):
        self.price = price
        self.work = work
