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
        possibleFullRows = fileCount // self.rowCount
        remainderColumn = fileCount % self.rowCount

        if remainderColumn == 0:
            columnCount = possibleFullRows
        elif remainderColumn > 0:
            columnCount = possibleFullRows + 1
        else:
            columnCount = 0

        for num in range(self.rowCount):
            l = [f"{num + 1}. {files[num]}"]
            try:
                for i in range(possibleFullRows):  # loops over every complete column
                    if possibleFullRows - 1 > i:
                        l.append(f"{num + self.rowCount + 1 + i}. {files[num + self.rowCount + i]}")
                    # elif num == i:
                    #     l.append(f"{num + self.rowCount + 2 + i}. {files[num + self.rowCount + i]}")

                print("          ".join(l))
            except IndexError:
                print("".join(l))
                # prints item in column without anything in line

    # def downLevel(self):
    #     down = os.listdir("/..")
    #     print(down)


util = LineUtil(".", False, 4)
util.upLevel()
