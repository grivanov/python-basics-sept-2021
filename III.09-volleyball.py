from math import floor

year_type = input()
holiday = int(input())
hometown_weekends = int(input())

games_sofia = ((48 - hometown_weekends) * 0.75) + ((2 / 3) * holiday)
games_hometown = hometown_weekends

total_games = games_sofia + games_hometown

if year_type == "leap":
    total_games = floor(total_games + total_games * 0.15)
else:
    total_games = floor(total_games)

print(total_games)
