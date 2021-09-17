a = int(input())
b = int(input())

max_pieces = a * b
taken_pieces_sum = 0

while True:

    taken_pieces = input()

    if taken_pieces == "STOP":
        break
    else:
        taken_pieces = int(taken_pieces)
        taken_pieces_sum += taken_pieces

        if taken_pieces_sum >= max_pieces:
            break

diff = max_pieces - taken_pieces_sum

if diff >= 0:
    print(f"{diff} pieces are left.")
else:
    print(f"No more cake left! You need {abs(diff)} pieces more.")
