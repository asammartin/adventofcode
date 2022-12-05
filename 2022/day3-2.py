totalPriority = 0
with open("day3.data") as f:
    for idx, line in enumerate(f):
        line = line.strip()
        groupPos = idx % 3
        items = {}
        for item in line:
            if groupPos == 0 or item in intersect:
                items[item] = item
        intersect = list(items.keys())
        if groupPos < 2:
            continue
        priority = ord(intersect[0]) - ord('a')
        if priority < 0:
            priority = priority + 32 + 26
        priority += 1
        totalPriority += priority
print(totalPriority)
