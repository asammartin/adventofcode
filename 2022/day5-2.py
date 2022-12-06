stacks = {}
with open("day5.stacks.data") as f:
    for line in f:
        if not line.strip():
            continue
        for idx in range(int(len(line) / 4)):
            col = (idx * 4) + 1
            if idx not in stacks:
                stacks[idx] = []
            box = line[col].strip()
            if box:
                stacks[idx].append(box)
for key in stacks.keys():
    print(key, stacks[key])
with open("day5.instructions.data") as f:
    for line in f:
        instructions = line.split()
        moveCnt = int(instructions[1])
        fromIdx = int(instructions[3])
        toIdx = int(instructions[5])
        boxes = stacks[fromIdx - 1][:moveCnt]
        del stacks[fromIdx - 1][:moveCnt]
        boxes.extend(stacks[toIdx - 1])
        stacks[toIdx - 1] = boxes
for key in stacks.keys():
    print(key, stacks[key])
output = ""
for key in stacks:
    output += stacks[key][0]
print(output)
