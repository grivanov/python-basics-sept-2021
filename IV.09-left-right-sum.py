loop = int(input())
double_loop = loop * 2
left = int()
right = int()
step = 1

for l in range(double_loop):
    curr_num = int(input())
    
    if step <= loop:
        left += curr_num
    else:
        right += curr_num
    
    step += 1

diff = right - left

if diff == 0:
    print(f"Yes, sum = {right}")
else:
    print(f"No, diff = {abs(diff)}")


