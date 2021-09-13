value = float(input())
source = input()
target = input()

temp_in_meters = 0
convert_result = 0

if source == "cm":
    temp_in_meters = value / 100
elif source == "mm":
    temp_in_meters = value / 1000
else:
    temp_in_meters = value

if target == "cm":
    convert_result = temp_in_meters * 100
elif target == "mm":
    convert_result = temp_in_meters * 1000
else:
    convert_result = temp_in_meters

print(f"{convert_result:.3f}")
