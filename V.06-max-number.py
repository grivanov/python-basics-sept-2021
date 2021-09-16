import sys

max_num = -sys.maxsize

while True:
    inp = input()

    if inp == "Stop":
        break
    else:
        inp = int(inp)

        if inp > max_num:
            max_num = inp

print(max_num)