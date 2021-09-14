from datetime import datetime
import time
import sys

fmt = '%Y-%m-%d %H:%M:%S'
dt_from = sys.argv[1]
dt_to = sys.argv[2]
d1 = datetime.strptime(dt_from, fmt)
d2 = datetime.strptime(dt_to, fmt)

# Convert to Unix timestamp
d1_ts = time.mktime(d1.timetuple())
d2_ts = time.mktime(d2.timetuple())

minutesDiff = int(d2_ts-d1_ts) / 60

print(minutesDiff)
