import string


class LC:
    # x = ' '
    y = ' '

    def __init__(x, msg):
        str(msg)

    def translate(x):
        x = msg.replace("a", "m")
        # x = y
        # print(y)
        print(x)


alphabet = list(string.ascii_lowercase)
m = input("Enter your message: ")

j = 0

n = " "
for i in m:
    for j in range(26):
        if i == alphabet[j]:
            if j in range(13):
                print(alphabet[j+13], end="")
            if j in range(13,26):
                print(alphabet[j - 13],end="")
        if i == ' ':
            print(n,end='')
