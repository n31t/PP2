import datetime
from datetime import datetime, time, timedelta, date

dt = date.today() - timedelta(1)
tmr = date.today() + timedelta(1)
print('Current Date :', date.today())
print('Yesterday :', dt)
print('Yesterday :', tmr)
