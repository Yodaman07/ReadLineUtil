import math
import os


# print(os.listdir(os.path.curdir))
# Current working directory is documents so ../ will bring you to the default directory by going up a level
class LineUtil:  # TODO close extra space if the first row has less than the desired number
    def __init__(self, path, rowCount, charLimit: int = None):
        self.path = path
        self.rowCount = rowCount
        self.charLimit = charLimit
        self.files = None

    def getLevel(self, direction, showHidden=False):  # directions are: up "/..", down f"/{name}", or current ""
        newPath = f"{self.path}" + direction

        self.path = newPath
        files = os.listdir(newPath)

        if not showHidden:
            returnFiles = files.copy()
            for i in files:
                if i.startswith("."):
                    returnFiles.remove(i)
            files = returnFiles

        self.files = files
        self.display(files)


    def display(self, files):
        fileCount = len(files)

        columns = math.ceil(fileCount / self.rowCount)
        remainderColumn = fileCount % self.rowCount
        # remainder column is how many files are under the last column
        # any files that don't divide evenly into the first set
        # NOT Column number
        self.display_formatted_text(files, columns, remainderColumn)

    def display_formatted_text(self, file_list, c_count, c_remainder):
        correctedNameList = self.correctedNames(file_list)

        length_list = correctedNameList.copy()
        length_list.sort(reverse=True, key=len)
        max_length = len(length_list[0])

        for row in range(self.rowCount):
            files = []
            if (row + 1 <= c_remainder) or (c_remainder == 0):  # checks for full row
                self.add_files(c_count, row, correctedNameList, max_length, files)
            else:
                self.add_files(c_count - 1, row, correctedNameList, max_length, files)
                # Subtract 1 because there is one less full column now
            print("         ".join(files))

    def correctedNames(self, file_list):
        if not self.charLimit:
            return file_list
        for index, file in enumerate(file_list):
            if len(file) > self.charLimit:
                fixedName = file[0:self.charLimit] + " (...)"
                file_list[index] = fixedName
        return file_list

    def add_files(self, c_count, row, file_list, max_length, files):  # adds a row of files
        for column in range(c_count):
            index = column * self.rowCount + row
            file = file_list[index]

            file += " " * (max_length - len(file))
            digitCount = len(str(index + 1))
            if digitCount > 1:
                file = file.removesuffix(" " * (int(digitCount) - 1))  # corrects spacing for numbers greater than 1
            files.append(f"{index + 1}. {file}")
