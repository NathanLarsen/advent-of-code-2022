with open("day4/input.txt") as file:
    total = 0
    for line in file:
        efl1, elf2 = [
            range(int(y[0]), int(y[1]) + 1)
            for y in [x.split("-") for x in line.strip().split(",")]
        ]
        # if (efl1.start in elf2 and efl1[-1] in elf2) or (elf2.start in efl1 and elf2[-1] in efl1):
        #     total += 1
        if (efl1.start in elf2 or efl1[-1] in elf2) or (elf2.start in efl1 or elf2[-1] in efl1):
            total += 1

print(total)