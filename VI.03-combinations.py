combination_result = int(input())
combination_count = 0

for a in range(0, combination_result + 1):
    for b in range(0, combination_result + 1):
        for c in range(0, combination_result + 1):
            if a + b + c == combination_result:
                combination_count += 1

print(combination_count)