import os
import math


# print(os.listdir(os.path.curdir))
# Current working directory is documents so ../ will bring you to the default directory by going up a level
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

        print(files)
        print(fileCount, columns, remainderColumn)  # remainder column is how many files are under the last column
        # any files that don't divide evenly into the first set
        # NOT Column number
        self.display_formatted_text(files, columns, remainderColumn)

    # def downLevel(self):
    #     down = os.listdir("/..")
    #     print(down)
    def display_formatted_text(self, file_list, c_count, c_remainder):
        length_list = file_list.copy()
        length_list.sort(reverse=True, key=len)
        max_length = len(length_list[0])
        for row in range(self.rowCount):
            files = []
            if (row + 1 <= c_remainder) or (c_remainder == 0):  # checks for full row
                self.add_files(c_count, row, file_list, max_length, files)
            else:
                self.add_files(c_count - 1, row, file_list, max_length, files)
                # Subtract 1 because there is one less full column now
            print("         ".join(files))

    def add_files(self, c_count, row, file_list, max_length, files): # adds a row of files
        for column in range(c_count):
            index = column * self.rowCount + row
            file = file_list[index]
            # while len(file) < max_length:
            #     file += " "
            file += " " * (max_length - len(file))
            digitCount = len(str(index+1))
            if digitCount > 1:
                file = file.removesuffix(" " * (int(digitCount)-1)) # corrects spacing for numbers greater than 1
            files.append(f"{index + 1}. {file}")


util = LineUtil(".", False, 6)
while True:
    direction = input("Find a new path: ")
    if direction == "up":
        util.upLevel()
