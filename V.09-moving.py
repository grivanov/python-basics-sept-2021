space_w = int(input())
space_l = int(input())
space_h = int(input())

space_volume = space_w * space_l * space_h
boxes_volume = 0

while boxes_volume <= space_volume:
    boxes = input()

    if boxes == "Done":
        break
    else:
        boxes = int(boxes)
        boxes_volume += boxes

diff = space_volume - boxes_volume

if diff > 0:
    print(f"{diff} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(diff)} Cubic meters more.")
