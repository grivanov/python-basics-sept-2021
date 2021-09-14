movie_type = input()
row = int(input())
col = int(input())

ticket_price = 0

if movie_type == "Premiere":
    ticket_price = 12
elif movie_type == "Normal":
    ticket_price = 7.5
else:
    ticket_price = 5

result = (row * col) * ticket_price

print(f"{result:.2f} leva")
