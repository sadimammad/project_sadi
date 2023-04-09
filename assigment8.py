from datetime import date, datetime, timedelta

a = input()
arr = a.split('/')
today = datetime.now()
day = date(int(arr[0]), int(arr[1]), int(arr[2]))
if today.month > day.month:
    print(today.year-day.year)
elif today.month == day.month:
    if today.day >= day.day:
        print(today.year-day.year)
    else:
        print(today.year-day.year-1)
else:
    print(today.year-day.year-1)
