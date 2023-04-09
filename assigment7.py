rom datetime import date, timedelta

day1 = date(2014, 7, 2)
day2 = date(2014, 7, 11)
diff = day2-day1
print(diff)
for i in range(1, diff.days):
    print(day1+timedelta(days=i))
