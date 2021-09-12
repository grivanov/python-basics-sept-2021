basketball_fee = int(input())
basketball_shoes = basketball_fee - (basketball_fee * 0.4)
basketball_uniform = basketball_shoes - (basketball_shoes * 0.2)
basketball_ball = basketball_uniform / 4
basketball_acc = basketball_ball / 5

total_price = basketball_fee + basketball_shoes + basketball_uniform + basketball_ball + basketball_acc

print(total_price)