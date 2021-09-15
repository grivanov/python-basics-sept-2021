import sys
loop = int(input())
max_num = -sys.maxsize
temp = 0
sum_num = 0

for l in range(0, loop):
    curr_num = int(input())

    if curr_num > max_num:
        max_num = curr_num
        sum_num += curr_num
    else:
        sum_num += curr_num

diff = max_num - (sum_num - max_num)

if sum_num - max_num == max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    print(f"Diff = {abs(diff)}")
