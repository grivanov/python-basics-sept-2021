pens_pkg = int(input())
markers_pkg = int(input())
liquid_volume = int(input())
pers_discount = int(input()) / 100

pens_price = pens_pkg * 5.80
markers_price = markers_pkg * 7.20
liquid_price = liquid_volume * 1.20

total_price = pens_price + markers_price + liquid_price
final_amount = total_price - (total_price * pers_discount)

print(final_amount)
