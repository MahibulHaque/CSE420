def validEmailAddress(s):
    state = 0
    email = False
    i = 0
    while (i < len(s)):
        match state:
            case 0:
                if (ord(s[i]) >= 65 and ord(s[i]) <= 90) or (ord(s[i]) >= 97 and ord(s[i]) <= 122):
                    state = 1
                else:
                    state = 6
                i += 1

            case 1:
                if (s[i] == '@'):
                    state = 2
                elif (ord(s[i]) >= 65 and ord(s[i]) <= 90) or (ord(s[i]) >= 97 and ord(s[i]) <= 122) or (ord(s[i]) >= 48 and ord(s[i]) <= 57):
                    state = 1
                else:
                    state = 6
                i += 1

            case 2:
                if (ord(s[i]) >= 65 and ord(s[i]) <= 90) or (ord(s[i]) >= 97 and ord(s[i]) <= 122):
                    state = 3
                else:
                    state = 6
                i += 1

            case 3:
                if (s[i] == '.'):
                    state = 4
                elif (ord(s[i]) >= 65 and ord(s[i]) <= 90) or (ord(s[i]) >= 97 and ord(s[i]) <= 122):
                    state = 3
                else:
                    state = 6
                i += 1

            case 4:
                if (ord(s[i]) >= 65 and ord(s[i]) <= 90) or (ord(s[i]) >= 97 and ord(s[i]) <= 122):
                    state = 5
                    email = True
                else:
                    state = 6
                i += 1

            case 5:
                if (ord(s[i]) >= 65 and ord(s[i]) <= 90) or (ord(s[i]) >= 97 and ord(s[i]) <= 122):
                    state = 5
                elif (s[i] == '.'):
                    state = 4
                else:
                    state = 6
                i += 1

            case 6:
                email = False
                if (s[i]):
                    state = 6
                i += 1

    return email


def validWebAddress(s):
    state = 0
    web = False
    i = 0
    while (i < len(s)):
        match state:
            case 0:
                if (s[i].lower() == 'w'):
                    state = 1
                else:
                    state = 8
                i += 1
            case 1:
                if (s[i].lower() == 'w'):
                    state = 2
                else:
                    state = 8
                i += 1
            case 2:
                if (s[i].lower() == 'w'):
                    state = 3
                else:
                    state = 8
                i += 1
            case 3:
                if (s[i] == '.'):
                    state = 4
                else:
                    state = 8
                i += 1
            case 4:
                if (ord(s[i]) >= 65 and ord(s[i]) <= 90) or (ord(s[i]) >= 97 and ord(s[i]) <= 122):
                    state = 5
                else:
                    state = 8
                i += 1
            case 5:
                if (ord(s[i]) >= 65 and ord(s[i]) <= 90) or (ord(s[i]) >= 97 and ord(s[i]) <= 122):
                    state = 5
                elif (s[i] == '.'):
                    state = 6
                else:
                    state = 8
                i += 1
            case 6:
                if (ord(s[i]) >= 65 and ord(s[i]) <= 90) or (ord(s[i]) >= 97 and ord(s[i]) <= 122):
                    web = True
                    state = 7
                else:
                    state = 8
                i += 1
            case 7:
                if (ord(s[i]) >= 65 and ord(s[i]) <= 90) or (ord(s[i]) >= 97 and ord(s[i]) <= 122):
                    state = 7
                elif (s[i] == '.'):
                    state = 6
                else:
                    state = 8
                i += 1
            case 8:
                web = False
                if (s[i]):
                    state = 8
                i += 1
    return web


if __name__ == "__main__":
    with open('Lab-2/input.txt', 'r') as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]
        lines.pop(0)

        for index, line in enumerate(lines):

            if validEmailAddress(line):
                print(f"Email, {index+1}")

            elif validWebAddress(line):
                print(f"Web, {index+1}")

            else:
                print(f"Invalid, {index+1}")
    f.close()
