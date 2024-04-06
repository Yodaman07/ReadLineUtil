import re
import LineUtil


class InputHandler:
    def __init__(self, lineUtil: LineUtil):
        self.cmd = None
        self.lineUtil = lineUtil

    def handleInput(self, cmd: str):
        self.cmd = cmd
        if self.getCmd() == "show":
            self.lineUtil.getLevel("", showHidden="a" in self.getFlags())
        if self.getCmd() == "move":
            self.evaluateFlags(self.getFlags())

    def getCmd(self):
        cmdRegex = re.compile(r"^(\w+)")
        cmd = cmdRegex.match(self.cmd)
        return cmd.group()

    def getFlags(self):
        flagRegex = re.compile(r"[-]([^ ]+)")
        flag = flagRegex.findall(self.cmd)
        return flag

    def evaluateFlags(self, flagList):
        showAll = False
        if "a" in flagList:
            showAll = True
        if ("u" and "d") in flagList:
            print("Error: cannot compute with two contradicting flags")
            return None

        for flag in flagList:
            if flag == "u":
                self.lineUtil.getLevel("/..", showAll)
            elif flag[0] == "d":
                num = int(flag[2:]) # Check for paired number
                fileName = self.lineUtil.files[num - 1]
                # Format would be 'd:10' for example
                self.lineUtil.getLevel("/" + fileName, showAll)
