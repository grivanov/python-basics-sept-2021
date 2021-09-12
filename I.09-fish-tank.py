l = int(input())
w = int(input())
h = int(input())
perc = float(input()) / 100

volume = l * w * h
litric_volume = volume * 0.001

result = litric_volume * (1 - perc)

print(result)
