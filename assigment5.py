from datetime import datetime, timedelta

day = datetime.now()
num = day.strftime('%Y-%m-%d')
print('Current Date:', day.strftime('%Y-%m-%d'))
subtracted = day-timedelta(days=5)
print('5 days before Current Date :', subtracted.strftime('%Y-%m-%d'))
