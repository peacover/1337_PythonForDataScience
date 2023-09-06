import datetime

old_time = datetime.datetime(1970, 1, 1)
current_time = datetime.datetime.now()
diff_seconds = (current_time - old_time).total_seconds()
str_diff_time = str(diff_seconds).split(".")
split_num_per_three = []
for i in range(len(str_diff_time[0]) - 3, -1, -3):
    split_num_per_three.insert(0, str_diff_time[0][i: i+3])
split_num_per_three.insert(0, str_diff_time[0][0: i])
split_num_per_three = ",".join(split_num_per_three) + "." + str_diff_time[1][:4]
scientific_notation = "{:.2e}".format(diff_seconds)

print(f"Seconds since January 1, 1970: {split_num_per_three} or {scientific_notation} in scientific notation")
print(f"{current_time.strftime('%b')} {current_time.day} {current_time.year}")