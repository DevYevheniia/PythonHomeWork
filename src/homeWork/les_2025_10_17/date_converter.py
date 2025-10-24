#DZ 6.2. Number to date converter
user_number = int(input("Number to convert : "))

days = user_number // 86400
remainder_days = user_number % 86400

hours = remainder_days // 3600
remainder_hours = remainder_days % 3600

minutes = remainder_hours // 60
seconds = remainder_hours % 60


hh = "0" + str(hours) if hours < 10 else str (hours)
mm = "0" + str(minutes) if minutes < 10 else str(minutes)
ss = "0" + str(seconds) if seconds < 10 else str(seconds)
print(f"{user_number} -> {days} days, {hours:02}:{minutes:02}:{seconds:02}" )