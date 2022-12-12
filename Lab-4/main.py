import re

f = open("Lab-4/input.txt", "r")

code = f.readlines()


method = []

mainMethod = r"public static void main(.*)"
reg = r"(public|private|default)( static)? (Boolean|char|byte|short|int|long|float|double|String|void) \w+\((.*)?\)"

for line in code:
    if re.match(reg, line) and not re.match(mainMethod, line):
        method.append(re.findall("(Boolean|char|byte|short|int|long|float|double|String|void) (\w+)\((.+)?\)", line)[0])
        
print("Methods:")
for m in method:
    print(f"{m[1]} ({m[2]}), return type: {m[0]}")