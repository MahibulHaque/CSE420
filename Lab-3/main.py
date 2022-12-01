import re

f = open("Lab-3/input.txt", "r")
code = f.readlines()
code = [x.strip() for x in code]
reg = []

n = code[0]
code.pop(0)

for j in range(int(n)):
    reg.append(code[j])

for j in range(int(n)):
    code.remove(reg[j])
    
code.pop(0)

for i in range(len(code)):
    matched = 0
    for j in range(len(reg)):
        if re.fullmatch(reg[j], code[i]):
            matched = 1
            print("YES,", j+1)
    if matched == 0:
        print("NO,", matched)