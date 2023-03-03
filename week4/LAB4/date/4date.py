import datetime
from datetime import datetime, time, timedelta, date

dt1 = datetime.strptime("2020-02-15 02:45:51", "%Y-%m-%d %H:%M:%S")
dt2 = datetime.now()
timedelta1 = dt2 - dt1
df = timedelta1.days * 24 * 3600 + timedelta1.seconds
print(f'{df} seconds')
