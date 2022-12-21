class Node:
    def __init__(self, isDir: bool, name, size=None) -> None:
        self.isDir = isDir
        self.name = name
        self.size = size
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_size(self):
        if self.isDir:
            totalSize = 0
            for child in self.children:
                totalSize += child.get_size()
            return totalSize
        else:
            return self.size
    
    def print_children(self,level):
        if self.isDir:
            print('--' * level + self.name + ' (total=' + str(self.get_size()) +')')
        else: 
            print('--' * level + self.name + ' (file=' + str(self.get_size()) +')')
        if len(self.children) > 0:
            for child in self.children:
                child.print_children(level+1)
    
    def find_subdirectories_part1(self):
        dirSizes = 0
        if self.isDir:
            for child in self.children:
                if child.isDir and child.get_size() <= 100000:
                    dirSizes += child.get_size() + child.find_subdirectories_part1()
                else:
                    dirSizes += child.find_subdirectories_part1()
        return dirSizes

class Tree:
    def __init__(self) -> None:
        self.root = Node(isDir=True, name="root")
        self.current = self.root

    def reset_to_root(self):
        self.current = self.root

    def go_up_one_level(self):
        self.current = self.current.parent

    def go_to_child(self, name):
        self.current = list(filter(lambda child: child.name == name, self.current.children))[0]

    def add_new_child(self, child):
        self.current.add_child(child)
    


if __name__ == "__main__":        
    with open('input.txt', 'r') as f:
        values = f.readlines()
        values = [i.strip() for i in values]
    
    treeObject = Tree()

while len(values) > 0:
    line = values.pop(0)
    if line == '$ cd /': 
        treeObject.reset_to_root()
    elif line == '$ ls':
        while len(values)>0 and '$' not in values[0]:
            line = values.pop(0)
            size, name = line.split(' ')
            if size.isdigit():
                newNode = Node(isDir=False, name=name, size=int(size))
            else:
                newNode = Node(isDir=True, name=name)
            treeObject.add_new_child(newNode)
    elif line == '$ cd ..':
        treeObject.go_up_one_level()
    elif '$ cd' in line:
        _, _, name = line.split(' ')
        treeObject.go_to_child(name)
    
    print(treeObject.root.find_subdirectories_part1())