loop = int(input())
p1, p2, p3 = 0, 0, 0

for l in range(loop):
    num = int(input())

    if num % 2 == 0:
        p1 +=1
    
    if num % 3 == 0:
        p2 +=1
    
    if num % 4 == 0:
        p3 += 1
    
print(f"{((p1 / loop) * 100):.2f}%")
print(f"{((p2 / loop) * 100):.2f}%")
print(f"{((p3 / loop) * 100):.2f}%")