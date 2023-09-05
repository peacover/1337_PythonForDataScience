import datetime

old_time = datetime.date(1970, 1, 1)
current_time = datetime.datetime.now()
print(current_time.timestamp(), old_time)