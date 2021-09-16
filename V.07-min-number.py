import sys

min_num = sys.maxsize

while True:
    inp = input()

    if inp == "Stop":
        break
    else:
        inp = int(inp)

        if inp < min_num:
            min_num = inp

print(min_num)