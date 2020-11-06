import calendar

date = input().split(" ")
# date = "08 05 2015".split(" ")
month = int(date[0])
day = int(date[1])
year = int(date[2])

print(list(calendar.day_name)[calendar.weekday(year, month, day)].upper())
