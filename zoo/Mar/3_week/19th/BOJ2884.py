hour, minute = map(int, input().split())

total_time = hour * 60 + minute
real_time = total_time - 45

new_hour = (real_time // 60) % 24
new_minute = real_time % 60


print(new_hour, new_minute)
