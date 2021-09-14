temperature = int(input())
part_of_day = input()

outfit = ""
shoes = ""

if part_of_day == "Morning":
    if temperature >= 10 and temperature <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif temperature > 18 and temperature <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif temperature >= 25:
        outfit = "T-Shirt"
        shoes = "Sandals"

elif part_of_day == "Afternoon":
    if temperature >= 10 and temperature <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif temperature > 18 and temperature <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif temperature >= 25:
        outfit = "Swim Suit"
        shoes = "Barefoot"

else:
    outfit = "Shirt"
    shoes = "Moccasins"

print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")
