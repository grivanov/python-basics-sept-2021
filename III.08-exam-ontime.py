from math import floor

exam_hour = int(input())
exam_minutes = int(input())
arrive_hour = int(input())
arrive_minutes = int(input())
status = ""

exam_in_mins = exam_hour * 60 + exam_minutes  # 9.30 = 570
arrive_in_mins = arrive_hour * 60 + arrive_minutes  # 9.50 = 590

diff = arrive_in_mins - exam_in_mins

if diff == 0 or (diff >= -30 and diff <= 0):
    status = "On time"

    print(status)

    if diff != 0:
        print(f"{abs(diff)} minutes before the start")


    
elif diff <= -30:
    status = "Early"

    print(status)

    if diff >= -59 and diff <= 0:
        print(f"{abs(diff)} minutes before the start")
    elif diff <= -60:
        diff_h = floor(abs(diff) / 60)
        diff_m = abs(diff) % 60

        if diff_m < 10:
            print(f"{diff_h}:0{diff_m} hours before the start")
        else:
            print(f"{diff_h}:{diff_m} hours before the start")

else:
    status = "Late"

    print(status)

    if diff > 0 and diff <= 59:
        print(f"{abs(diff)} minutes after the start")
    elif diff >= 60:
        diff_h = floor(diff / 60)
        diff_m = diff % 60

        if diff_m < 10:
            print(f"{diff_h}:0{diff_m} hours after the start")
        else:
            print(f"{diff_h}:{diff_m} hours after the start")

