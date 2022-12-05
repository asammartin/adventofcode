totalOverlapPairs = 0
with open("day4.data") as f:
    for line in f:
        pair = line.strip().split(",")
        left = [int(x) for x in pair[0].split("-")]
        right = [int(x) for x in pair[1].split("-")]
        if left[0] <= right[1] and left[1] >= right[0]:
            totalOverlapPairs += 1
        elif right[0] <= left[1] and right[1] >= left[0]:
            totalOverlapPairs += 1
print(totalOverlapPairs)
