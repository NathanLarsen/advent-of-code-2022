with open('day3/input.txt', 'r', encoding='utf-8') as input:
    total = 0
    values = {'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8,
    'i':9,
    'j':10,
    'k':11,
    'l':12,
    'm':13,
    'n':14,
    'o':15,
    'p':16,
    'q':17,
    'r':18,
    's':19,
    't':20,
    'u':21,
    'v':22,
    'w':23,
    'x':24,
    'y':25,
    'z':26,
    'A':27,
    'B':28,
    'C':29,
    'D':30,
    'E':31,
    'F':32,
    'G':33,
    'H':34,
    'I':35,
    'J':36,
    'K':37,
    'L':38,
    'M':39,
    'N':40,
    'O':41,
    'P':42,
    'Q':43,
    'R':44,
    'S':45,
    'T':46,
    'U':47,
    'V':48,
    'W':49,
    'X':50,
    'Y':51,
    'Z':52
    }
    # for line in input.readlines():
    #     half = int(len(line) / 2)
    #     firstHalf, secondHalf = line[:half], line[half:]
    #     for char in firstHalf:
    #         if(char in secondHalf):
    #             print(char)
    #             total += values[char]
    #             break
    lines = input.readlines()
    for i in range(0, len(lines), 3):
        elf1 = lines[i].strip()
        elf2 = lines[i + 1].strip()
        elf3 = lines[i + 2].strip()
        for char in elf1:
            if(char in elf2 and char in elf3):
                total += values[char]
                break
    print(total)