month = input()
nights_stay = int(input())

studio_price = 0
apart_price = 0

if month == "May" or month == "October":
    apart_price = 65
    studio_price = 50
    if nights_stay > 14:
        studio_price -= studio_price * 0.3
        apart_price -= apart_price * 0.1
    elif nights_stay > 7:
        studio_price -= studio_price * 0.05

elif month == "June" or month == "September":
    apart_price = 68.70
    studio_price = 75.20

    if nights_stay > 14:
        studio_price -= studio_price * 0.2
        apart_price -= apart_price * 0.1

else:
    apart_price = 77
    studio_price = 76

    if nights_stay > 14:
        apart_price -= apart_price * 0.1

print(f"Apartment: {(apart_price * nights_stay):.2f} lv.")
print(f"Studio: {(studio_price * nights_stay):.2f} lv.")
