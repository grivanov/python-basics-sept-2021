budget = float(input())
season = input()
destination = ""
holiday_type = ""
used_money = 0

if budget <= 100:
    destination = "Bulgaria"

    if season == "summer":
        used_money = budget * 0.3
        holiday_type = "Camp"
    else:
        used_money = budget * 0.7
        holiday_type = "Hotel"


elif budget <= 1000:
    destination = "Balkans"

    if season == "summer":
        used_money = budget * 0.4
        holiday_type = "Camp"
    else:
        used_money = budget * 0.8
        holiday_type = "Hotel"

else:
    destination = "Europe"

    used_money = budget * 0.9
    holiday_type = "Hotel"

print(f"Somewhere in {destination}")
print(f"{holiday_type} - {used_money:.2f}")
