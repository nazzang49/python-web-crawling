from datetime import datetime

current_time = datetime.now()

print("current_time date and time : " + str(current_time))
print("current_time year : " + str(current_time.year))
print("current_time month : " + str(current_time.month))
print("current_time day : " + str(current_time.day))
print("current_time hour : " + str(current_time.hour))
print("current_time min : " + str(current_time.minute))
print("current_time second : " + str(current_time.second))
print("current_time date : {}-{}-{}".format(current_time.year, current_time.month, current_time.day))

# get today
t = ["월", "화", "수", "목", "금", "토", "일"]
r = datetime.today().weekday()
print(t[r])
