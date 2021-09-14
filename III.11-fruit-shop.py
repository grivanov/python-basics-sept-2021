item = input()
day = input()
quantity = float(input())

items = ["banana", "apple", "orange",
         "grapefruit", "kiwi", "pineapple", "grapes"]
days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
price_for_item = 0

if item in items and day in days:

    if day in ["Saturday", "Sunday"]:
        if item == "banana":
            price_for_item = 2.70
        elif item == "apple":
            price_for_item = 1.25
        elif item == "orange":
            price_for_item = 0.90
        elif item == "grapefruit":
            price_for_item = 1.60
        elif item == "kiwi":
            price_for_item = 3.00
        elif item == "pineapple":
            price_for_item = 5.60
        elif item == "grapes":
            price_for_item = 4.20
    else:
        if item == "banana":
            price_for_item = 2.50
        elif item == "apple":
            price_for_item = 1.20
        elif item == "orange":
            price_for_item = 0.85
        elif item == "grapefruit":
            price_for_item = 1.45
        elif item == "kiwi":
            price_for_item = 2.70
        elif item == "pineapple":
            price_for_item = 5.50
        elif item == "grapes":
            price_for_item = 3.85

    result = price_for_item * quantity
    print(f"{result:.2f}")

else:
    print("error")
