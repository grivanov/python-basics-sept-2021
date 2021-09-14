hour = int(input())
day = input()

workdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

if hour >= 10 and hour < 18 and day in workdays:
    print("open")
else:
    print("closed")