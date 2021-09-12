deposit_money = float(input())
deposit_length = float(input())
yearly_interest = float(input())

overall_interest = deposit_money * (yearly_interest / 100)
one_month_interest = overall_interest / 12

final_sum = deposit_money + (deposit_length * one_month_interest)

print(final_sum)