import math

columns = []
columnsums = []
rowvalues = []
rowcount = 0
with open("test.data") as f:
    for line in f:
        line = line.strip()
        for c in range(len(line)):
            if (rowcount == 0):
                columns.append([])
                columnsums.append(0)
                rowvalues.append(0)
            intval = int(line[c])
            columns[c].append(intval)
            columnsums[c] += intval
            rowvalue = 0
        rowcount += 1
    midway = rowcount / 2
    gamma = 0
    epsilon = 0
    cslen = len(columnsums)
    for i in range(cslen):
        exp = cslen - i - 1
        val = math.pow(2, exp)
        if (columnsums[i] > midway):
            gamma += val
        else:
            epsilon += val
    consumption = gamma * epsilon
    print(f'gamma: {gamma} - epsilon: {epsilon} - consumption: {consumption}')
