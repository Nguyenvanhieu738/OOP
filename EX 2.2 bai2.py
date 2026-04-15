r = 5   # ý 1
sphere = (4/3) * 3.14 * r**3 
print("sphere= ", sphere ,"(r=5)")

price = 24.95   # ý 2
price_after = price - price * 0.4
ship_cost = 3 + 59*0.75
total_cost = price_after * 60 + ship_cost
print("total cost= ", total_cost)


## sáng là 6h52 = 6 giờ 52 phút 
# chạy 1 dặm với thời gian là 8 phút 15 giây mỗi dặm 
# chạy 3 dặm với thời gian là 7 phút 12 giây mỗi dặm 
# sau đó chạy tiếp 1 dặm với tg là 8 phút 15 giây #27006s= 450,1p
# hỏi mấy h về tới nhà 
hours_start = 6*3600
minutes_start = 52*60 #quy ra giây 
start_time_seconds = hours_start + minutes_start 
total_seconds_start = hours_start + minutes_start
easy_pace_seconds = 8*60 + 15
tempo_pace_seconds = 7*60 + 12
easy_pace = 2
tempo_pace = 3
total_easy_pace_seconds = easy_pace * easy_pace_seconds
total_tempo_pace_seconds = tempo_pace * tempo_pace_seconds
home_time_seconds = total_easy_pace_seconds + total_tempo_pace_seconds + start_time_seconds
home_hours = home_time_seconds // 3600
seconds_remaining = home_time_seconds % 3600
home_minutes = seconds_remaining // 60
home_seconds = seconds_remaining % 60
print("timeforbreakfast= ", home_hours , home_minutes , home_seconds )