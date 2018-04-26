
from Rake import *
from Shovel import *
from Secateur import *


class DepartmentManager:
    tools = []

    def __init__(self):
        pass

    def sortByInstrument(self):
        self.tools.sort(key=lambda t: t.tool_type.name)

    def findByInstrument(self, worktype, tooltype):
        founded_tools = []
        for tool in self.tools:
            if tool.work == worktype and tool.tool_type == tooltype:
                founded_tools.append(tool)

        return founded_tools


if __name__ == '__main__':
    manager = DepartmentManager()

    rake = Rake(16.5, Work.TAKE_LEAVES)
    shovel = Shovel(14.5, Work.DIG_GROUND)
    secateur = Secateur(200, Work.CUT_BRANCHES)

    manager.tools = [rake, shovel, secateur]

    tools = manager.findByInstrument(Work.DIG_GROUND, ToolType.SHOVEL)
    for tool in tools:
        print(str(tool))
    print('\n')
    manager.sortByInstrument()
    import pdb; pdb.set_trace()
    for tool in manager.tools:
        print(str(tool))