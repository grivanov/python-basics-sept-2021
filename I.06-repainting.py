nylon_amount = int(input()) + 2
paint_amount = int(input())
paint_amount = paint_amount + (paint_amount * 0.10)
thinner_amount = int(input())
hours = int(input())
bags_price = 0.40

nylon_sum = nylon_amount * 1.50
paint_sum = paint_amount * 14.50
thinner_sum = thinner_amount * 5

materials_sum = nylon_sum + paint_sum + thinner_sum + bags_price

workers_hourly_price = materials_sum * 0.3
workers_price = workers_hourly_price * hours

final_price = materials_sum + workers_price

print(final_price)
