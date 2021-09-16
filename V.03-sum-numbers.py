limit = int(input())
numbers_sum = 0

while not(numbers_sum >= limit):
    data = int(input())
    numbers_sum += data

print(numbers_sum)