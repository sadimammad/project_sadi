from datetime import datetime, timedelta

day = datetime.now()
for i in range(5):
    print(day+timedelta(days=i))
