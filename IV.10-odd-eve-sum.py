loop = int(input())
even_sum = int()
odd_sum = int()

for number in range(1, loop + 1):
    curr_num = int(input())

    if number % 2 == 0:
        even_sum += curr_num
    else:
        odd_sum += curr_num

diff = even_sum - odd_sum

if diff == 0:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    print("No")
    print(f"Diff = {abs(diff)}")
