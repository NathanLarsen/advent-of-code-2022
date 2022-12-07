with open("day4/input.txt") as file:
    total = 0
    for line in file:
        elf1, elf2 = [
            range(int(y[0]), int(y[1]) + 1)
            for y in [x.split("-") for x in line.strip().split(",")]
        ]
        # if (elf1.start in elf2 and elf1[-1] in elf2) or (elf2.start in elf1 and elf2[-1] in elf1):
        #     total += 1
        if (elf1.start in elf2 or elf1[-1] in elf2) or (elf2.start in elf1 or elf2[-1] in elf1):
            total += 1

print(total)