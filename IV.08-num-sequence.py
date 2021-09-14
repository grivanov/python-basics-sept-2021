import sys

loops = int(input())
max = -sys.maxsize
min = sys.maxsize

for num in range(0, loops):
    n = int(input())

    if n >= max:
        max = n
    
    if n <= min:
        min = n

print(f"Max number: {max}")
print(f"Min number: {min}")
