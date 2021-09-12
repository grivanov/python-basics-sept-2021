from math import *


chicken_count = int(input())
fish_count = int(input())
veget_count = int(input())
delivery_price = 2.5

chicken_price = chicken_count * 10.35
fish_price = fish_count * 12.40
veget_price = veget_count * 8.15

total_sum = chicken_price + fish_price + veget_price

dessert_price = total_sum * 0.20

final_sum = total_sum + dessert_price + delivery_price

print(round(final_sum, 2))
