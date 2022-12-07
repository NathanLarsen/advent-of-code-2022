with open('day6/input.txt', 'r', encoding='utf-8') as input:
    s = input.readline()
    # for i in range(len(s) - 3):
    #     mySet = {s[i], s[i+1], s[i+2], s[i+3]}
    #     if(len(mySet) == 4):
    #         print(i + 4)
    #         break
    for i in range(len(s) - 13):
        mySet = {s[i], s[i+1], s[i+2], s[i+3], s[i+4], s[i+5], s[i+6], s[i+7], s[i+8], s[i+9], s[i+10], s[i+11], s[i+12], s[i+13]}
        if(len(mySet) == 14):
            print(i + 14)
            break
