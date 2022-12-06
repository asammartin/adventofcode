def containsDuplicate(charCnt = {}):
    for value in charCnt.values():
        if value > 1:
            return True
    return False

totalChars = 0
with open("day6.data") as f:
    for line in f:
        buffer = []
        charCnt = {}
        line = line.strip()
        print(line)
        for charPos, char in enumerate(line):
            if char not in charCnt:
                charCnt[char] = 0
            charCnt[char] += 1
            buffer.append(char)
            if len(buffer) < 4:
                continue
            if not containsDuplicate(charCnt):
                break
            out = buffer.pop(0)
            charCnt[out] -= 1
        totalChars += charPos + 1
        print(charPos + 1)
        print(buffer)
        print(charCnt)
print(totalChars)
