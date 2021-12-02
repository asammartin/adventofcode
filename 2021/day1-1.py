
NO_PREVIOUS_MEASUREMENT = -1

depthReport = []
with open("day1-1.data") as f:
    depthReport = [int(line.strip()) for line in f]

previousDepth = NO_PREVIOUS_MEASUREMENT
numIncrease = 0
for depth in depthReport:
    depthIncreased = depth > previousDepth
    if (previousDepth == NO_PREVIOUS_MEASUREMENT):
        print(f'{depth} (N/A - no previous measurement)')
    elif(depth < previousDepth):
        print(f'{depth} (decreased)')
    elif(depth > previousDepth):
        numIncrease += 1
        print(f'{depth} (increased)')
    else:
        print(f'{depth} (no change)')
    previousDepth = depth

print(numIncrease)
