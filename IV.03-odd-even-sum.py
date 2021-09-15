import sys

loop = int(input())
odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize

for l in range(1, loop + 1):
    num = float(input())

    if l % 2 == 0:
        even_sum += num

        if num > even_max:
            even_max = num

        if num < even_min:
            even_min = num

    else:
        odd_sum += num

        if num > odd_max:
            odd_max = num

        if num < odd_min:
            odd_min = num


print(f"OddSum={odd_sum:.2f},")
if odd_min == sys.maxsize or odd_max == -sys.maxsize:
    print(f"OddMin=No,")
    print(f"OddMax=No,")
else:
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")

print(f"EvenSum={even_sum:.2f},")

if even_min == sys.maxsize or even_max == -sys.maxsize:
    print(f"EvenMin=No,")
    print(f"EvenMax=No")
else:
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")
