open_tabs = int(input())
salary = int(input())

for t in range(open_tabs):
    tab = input()

    if salary == 0:
        break
    else:
        if tab == "Facebook":
            salary -= 150
        elif tab == "Instagram":
            salary -= 100
        elif tab == "Reddit":
            salary -= 50

if salary == 0:
    print("You have lost your salary.")
else:
    print(salary)

