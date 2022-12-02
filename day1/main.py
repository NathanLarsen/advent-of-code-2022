with open('input.txt', 'r', encoding='utf-8') as input:
    calmax = [0, 0, 0]
    temp = 0
    for line in input.readlines():
        if line.strip():
            temp += int(line)
        else:
            calmax.sort()
            if(temp > calmax[0]):
                calmax[0] = temp
            temp = 0
    print(f"Top 3 elves had {calmax} calories")
