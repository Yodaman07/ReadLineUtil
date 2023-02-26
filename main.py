import os
import math


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
        columns = math.ceil(fileCount / self.rowCount)
        remainderColumn = fileCount % self.rowCount
        self.display_formatted_text(files, columns, remainderColumn)

    # def downLevel(self):
    #     down = os.listdir("/..")
    #     print(down)
    def display_formatted_text(self, file_list, c_count, c_remainder):
        print(len(file_list))
        length_list = file_list.copy()
        length_list.sort(reverse=True, key=len)
        max_length = len(length_list[0])
        for row in range(self.rowCount):
            files = []
            if (row + 1 <= c_remainder) or (c_remainder == 0):  # checks for full row
                self.add_file(c_count, row, file_list, max_length, files)
            else:
                self.add_file(c_count + 1, row, file_list, max_length, files)
            print("         ".join(files))

    def add_file(self, c_count, row, file_list, max_length, files):
        for column in range(c_count):
            index = column * self.rowCount + row
            file = file_list[index]
            while len(file) < max_length:
                file += " "
            files.append(f"{index + 1}. {file}")


util = LineUtil(".", False, 6)
util.upLevel()
