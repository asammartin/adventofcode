totalOverlapPairs = 0
with open("day4.data") as f:
    for idx, line in enumerate(f):
        pair = line.strip().split(",")
        left = [int(x) for x in pair[0].split("-")]
        right = [int(x) for x in pair[1].split("-")]
        if left[0] >= right[0] and left[1] <= right[1]:
            totalOverlapPairs += 1
        elif right[0] >= left[0] and right[1] <= left[1]:
            totalOverlapPairs += 1
print(totalOverlapPairs)
