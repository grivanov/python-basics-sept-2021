vacation_days = int(input())
vacation_nights = vacation_days - 1
room_type = input()
feedback = input()
room_price = 0
vacation_sleep_price = 0

if room_type == "room for one person":
    room_price = 18
    vacation_sleep_price = vacation_nights * room_price

elif room_type == "apartment":
    room_price = 25
    vacation_sleep_price = vacation_nights * room_price

    if vacation_days < 10:
        vacation_sleep_price -= vacation_sleep_price * 0.3
    elif vacation_days >= 10 and vacation_days <= 15:
        vacation_sleep_price -= vacation_sleep_price * 0.35
    else:
        vacation_sleep_price -= vacation_sleep_price * 0.5

elif room_type == "president apartment":
    room_price = 35
    vacation_sleep_price = vacation_nights * room_price

    if vacation_days < 10:
        vacation_sleep_price -= vacation_sleep_price * 0.1
    elif vacation_days >= 10 and vacation_days <= 15:
        vacation_sleep_price -= vacation_sleep_price * 0.15
    else:
        vacation_sleep_price -= vacation_sleep_price * 0.2


if feedback == "positive":
    vacation_sleep_price += vacation_sleep_price * 0.25
else:
    vacation_sleep_price -= vacation_sleep_price * 0.1

print(f"{vacation_sleep_price:.2f}")
