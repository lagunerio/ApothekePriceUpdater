import csv

class FileReader():
    def __init__(self, filepath):
        self.filepath = filepath
        self.filedata = []

    def csvReadFile(self):
        with open(self.filepath, 'r') as file:
            data = csv.reader(file)
            for d in data:
                self.filedata.append(d)
        return self.filedata

    def GetContent(self):
        return self.filedata
