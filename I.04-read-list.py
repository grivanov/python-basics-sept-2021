from math import floor

book_pages = int(input())
pages_per_hour = int(input())
days_to_read = int(input())

read_time = floor(book_pages / pages_per_hour)

print(int(read_time / days_to_read))
