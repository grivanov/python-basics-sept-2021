from math import floor

record_in_seconds = float(input())
distance = float(input())
meter_speed_in_secs = float(input())

swimming_time = (floor(distance / 15) * 12.5) + (distance * meter_speed_in_secs)

difference = record_in_seconds - swimming_time

if difference > 0:
    print(
        f"Yes, he succeeded! The new world record is {swimming_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(difference):.2f} seconds slower.")
