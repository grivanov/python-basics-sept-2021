start = int(input())
end = int(input())
compare = int(input())
count = 0
is_found = False

for i in range(start, end + 1):
    for j in range(start, end + 1):
        count += 1

        if i + j == compare:
            is_found = True
            break

    if is_found:
        break


if not(is_found):
    print(f"{count} combinations - neither equals {compare}")
else:
    print(f"Combination N:{count} ({i} + {j} = {compare})")
