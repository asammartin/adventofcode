fileTree = {"type": "dir", "name": "/", "children": {}, "parent": None, "size": 0}
currentDir = fileTree
with open("day7.data") as f:
    for line in f:
        line = line.strip()
        tokens = line.split()
        if tokens[0] == "$":
            if tokens[1] == "cd":
                if tokens[2] == "/":
                    currentDir == fileTree
                elif tokens[2] == "..":
                    currentDir = currentDir["parent"]
                else:
                    currentDir = currentDir["children"][tokens[2]]
        elif tokens[0] == "dir":
            node = {"type": "dir", "name": tokens[1], "children": {}, "parent": currentDir, "size": 0}
            currentDir["children"][tokens[1]] = node
        else:
            node = {"type": "file", "name": tokens[1], "children": {}, "parent": currentDir, "size": int(tokens[0])}
            currentDir["children"][tokens[1]] = node

def fillSize(tree):
    for child in tree["children"].values():
        if child["type"] == "dir":
            tree["size"] += fillSize(child)
        else:
            tree["size"] += child["size"]
    return tree["size"]

fillSize(fileTree)

def printTree(tree, depth = "-"):
    print(depth, tree["name"], "(" + tree["type"] + ", size=" + str(tree["size"]) + ")")
    for child in tree["children"].values():
        printTree(child, " " + depth)

printTree(fileTree)

def calcTotalSize(tree, runningSize = 0):
    if tree["type"] == "dir":
        if tree["size"] <= 100000:
            runningSize += tree["size"]
        for child in tree["children"].values():
            runningSize += calcTotalSize(child)
    return runningSize

print("totalSize", calcTotalSize(fileTree))
