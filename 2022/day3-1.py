totalPriority = 0
with open("day3.data") as f:
    for line in f:
        line = line.strip()
        sackSize = int(len(line)/2)
        intersect = []
        left = {}
        for leftItem in line[:sackSize]:
            left[leftItem] = leftItem
        intersect = {}
        for rightItem in line[sackSize:]:
            if rightItem in left:
                intersect[rightItem] = rightItem
        intersect = list(intersect.keys())
        priority = ord(intersect[0]) - ord('a')
        if priority < 0:
            priority = priority + 32 + 26
        priority += 1
        totalPriority += priority
print(totalPriority)
