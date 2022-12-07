input_file = 'input.txt'

class File:
    def __init__(self, name, size):
        self.Name = name
        self.Size = size

    def toString(self, tabCount = 0):
        tabs = '  ' * tabCount
        return f"{tabs}- {self.Name} (file, size={self.Size})"

class Directory:
    def __init__(self, name):
        self.Name = name
        self.Directories = {}
        self.Files = {}
        self.Parent = None

    def AddFile(self, file):
        self.Files[file.Name] = file
        return self

    def AddDirectory(self, directory):
        self.Directories[directory.Name] = directory
        directory.Parent = self
        return self

    def FindDirectory(self, dirName):
        return self.Directories[dirName]

    def GetSize(self):
        size = sum([f.Size for f in self.Files.values()])
        size += sum([d.GetSize() for d in self.Directories.values()])
        return size

    def GetUndersizeDirectories(self, threshold):
        dirs = [d for d in self.Directories.values() if d.GetSize() <= threshold]
        [dirs.extend(d.GetUndersizeDirectories(threshold)) for d in self.Directories.values()]
        return list(dirs)

    def print(self):
        content = self.toString(0)
        print(content)
        return self

    def toString(self, tabCount):
        tabs = '  ' * tabCount
        content = f"{tabs}- {self.Name} (dir, GetSize()={self.GetSize()})\n"
        content += '\n'.join([f"{f.toString(tabCount + 1)}" for f in self.Files.values()]) + ('\n' if len(self.Directories) > 0 else '')
        content += '\n'.join([f"{d.toString(tabCount + 1)}" for d in self.Directories.values()])
        return content

output = open(input_file).read().split('\n')
output.pop(0)
rootDir = Directory('/')
currentDir = rootDir
for line in output:
    if line.startswith('$ cd'):
        dirName = line[5:]            
        if dirName == '..':
            currentDir = currentDir.Parent
            continue
        currentDir = currentDir.FindDirectory(dirName)
        continue

    if line.startswith('dir '):
        dirName = line[4:]            
        currentDir.AddDirectory(Directory(dirName))
        continue

    if line.startswith('$ ls'):
        continue

    # else it's a file
    parts = line.split(' ')
    currentDir.AddFile(File(parts[1], int(parts[0])))

underSizedDirs = rootDir.GetUndersizeDirectories(100000)
print(sum([d.GetSize() for d in underSizedDirs]))