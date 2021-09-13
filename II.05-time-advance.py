hour = int(input())
minutes = int(input())

new_hour = 0
new_minutes = 0

if minutes + 15 >= 60:
    new_minutes = (minutes + 15) - 60
    new_hour = hour + 1
else:
    new_minutes = minutes + 15
    new_hour = hour

if new_hour > 23:
    new_hour = 0


if new_minutes < 10:
    print(f"{new_hour}:0{new_minutes}")
else:
    print(f"{new_hour}:{new_minutes}")
