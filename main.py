import os



# print(os.listdir(os.path.curdir))

class LineUtil:
    def __init__(self, path, showHidden, rowCount):
        self.path = path
        self.showHidden = showHidden
        self.rowCount = rowCount

    def upLevel(self):
        newPath = f"{self.path}/.."
        self.path = newPath
        files = os.listdir(newPath)

        if not self.showHidden:
            returnFiles = files.copy()
            for i in files:
                if i.startswith("."):
                    returnFiles.remove(i)
            files = returnFiles

        fileCount = len(files)
        possibleFullColumns = fileCount // self.rowCount
        remainderColumn = fileCount % self.rowCount

        for count, row in enumerate(self.rowCount-1):
            l = [f"{count+1}. {files[count]}"]



        # print(files)

    # def downLevel(self):
    #     down = os.listdir("/..")
    #     print(down)


util = LineUtil(".", False, 5)
util.upLevel()




