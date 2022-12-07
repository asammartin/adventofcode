def parseTree(filename):
    root = {"type": "dir", "name": "/", "children": {}, "parent": None, "size": 0}
    curNode = root
    with open(filename) as f:
        for line in f:
            line = line.strip()
            tokens = line.split()
            if tokens[0] == "$":
                if tokens[1] == "cd":
                    if tokens[2] == "/":
                        curNode = root
                    elif tokens[2] == "..":
                        curNode = curNode["parent"]
                    else:
                        curNode = curNode["children"][tokens[2]]
            elif tokens[0] == "dir":
                node = {"type": "dir", "name": tokens[1], "children": {}, "parent": curNode, "size": 0}
                curNode["children"][tokens[1]] = node
            else:
                node = {"type": "file", "name": tokens[1], "children": {}, "parent": curNode, "size": int(tokens[0])}
                curNode["children"][tokens[1]] = node
    return root

def fillSize(tree):
    for child in tree["children"].values():
        if child["type"] == "dir":
            tree["size"] += fillSize(child)
        else:
            tree["size"] += child["size"]
    return tree["size"]

def printTree(tree, depth="-"):
    print(depth, tree["name"], "(" + tree["type"] + ", size=" + str(tree["size"]) + ")")
    for child in tree["children"].values():
        printTree(child, " " + depth)

def findSmallestGreaterThan(tree, running, mark):
    if tree["type"] == "dir":
        for child in tree["children"].values():
            running = findSmallestGreaterThan(child, running, mark)
        if tree["size"] < running["size"] and tree["size"] > mark:
            running = tree
    return running


fileTree = parseTree("day7.data")
fillSize(fileTree)
printTree(fileTree)

totalDiskSpace = 70000000
print("total disk space", totalDiskSpace)
updateSize = 30000000
print("update size", updateSize)
availableSpace = totalDiskSpace - fileTree["size"]
print("available space", availableSpace)
neededSpace = updateSize - availableSpace
print("needed space", neededSpace)
smallest = findSmallestGreaterThan(fileTree, fileTree, neededSpace)
print("smallest", smallest["name"], smallest["size"])
