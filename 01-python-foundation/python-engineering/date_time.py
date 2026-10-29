# datetime: use to work with date and time.
from datetime import datetime

breakdown_time = datetime.now()
print(breakdown_time)
print(breakdown_time.year)
print(breakdown_time.strftime("%d-%m-%y"))