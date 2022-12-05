elfCals = []
with open("day1.data") as f:
    elfCals.append(0)
    for line in f:
        cals = line.strip()
        if not cals:
            elfCals.append(0)
        else:
            elfCals[len(elfCals) - 1] += int(cals)
elfCals.sort(reverse=True)
print(elfCals)
print(elfCals[0])
print(elfCals[1])
print(elfCals[2])
print(elfCals[0]+elfCals[1]+elfCals[2])
