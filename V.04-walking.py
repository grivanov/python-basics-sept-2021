goal = 10000
steps_sum = 0

while True:
    steps = input()

    if steps == "Going home":
        steps = int(input())
        steps_sum += steps
        break    
    else:
        steps = int(steps)
        steps_sum += steps

        if steps_sum >= goal:
            break

diff = steps_sum - goal

if diff >= 0:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{abs(diff)} more steps to reach goal.")




