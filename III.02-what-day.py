day = input()
day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

if day in day_names:
    if day == "Saturday" or day == "Sunday":
        print("Weekend")
    else:
        print("Working day")
else:
    print("Error")