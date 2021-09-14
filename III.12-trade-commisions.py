city = input()
sales = float(input())

cities = ["Sofia", "Varna", "Plovdiv"]
percent_commision = 0

if city in cities and sales >= 0:

    if city == "Sofia":
        if sales >= 0 and sales <= 500:
            percent_commision = 5 / 100
        elif sales > 500 and sales <= 1000:
            percent_commision = 7 / 100
        elif sales > 1000 and sales <= 10000:
            percent_commision = 8 / 100
        else:
            percent_commision = 12 / 100

    elif city == "Varna":
        if sales >= 0 and sales <= 500:
            percent_commision = 4.5 / 100
        elif sales > 500 and sales <= 1000:
            percent_commision = 7.5 / 100
        elif sales > 1000 and sales <= 10000:
            percent_commision = 10 / 100
        else:
            percent_commision = 13 / 100

    else:
        if sales >= 0 and sales <= 500:
            percent_commision = 5.5 / 100
        elif sales > 500 and sales <= 1000:
            percent_commision = 8 / 100
        elif sales > 1000 and sales <= 10000:
            percent_commision = 12 / 100
        else:
            percent_commision = 14.5 / 100

    result = sales * percent_commision
    print(f"{result:.2f}")

else:
    print("error")