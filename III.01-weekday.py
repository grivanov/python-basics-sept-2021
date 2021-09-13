day = int(input())
day_names = ["Error", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

if day in range(1, 8):
    print(day_names[day])
else:
    print(day_names[0])