loop = int(input())
p1, p2, p3, p4, p5 = 0, 0, 0, 0, 0

for l in range(loop):
    n = int(input())

    if n < 200:
        p1 += 1
    elif n >= 200 and n <= 399:
        p2 += 1
    elif n >= 400 and n <= 599:
        p3 += 1
    elif n >= 600 and n <= 799:
        p4 += 1
    else:
        p5 += 1

print(f"{((p1 / loop) * 100):.2f}%")
print(f"{((p2 / loop) * 100):.2f}%")
print(f"{((p3 / loop) * 100):.2f}%")
print(f"{((p4 / loop) * 100):.2f}%")
print(f"{((p5 / loop) * 100):.2f}%")
