#!/usr/bin/python3

# show schedule for cron jobs in crontab

import subprocess
import os
from croniter import croniter
from datetime import datetime
import dateutil.tz
import io

# Get current time
tz = dateutil.tz.gettz('Africa/Johannesburg') #OlsonNames
base = subprocess.getoutput(["date +'%Y,%-m,%-d,%-H,%-M'"])
base2=base.split(',')
base3=datetime(int(base2[0]),int(base2[1]),int(base2[2]),int(base2[3]),int(base2[4]),tzinfo=tz)

# Extract cronjobs:
cron=subprocess.getoutput(["crontab -l"])
jobs={}
for line in io.StringIO(cron):
    if(line[0]!="#" and line[0].isalpha()==False):
        l=repr(line).split(' ')
        #cronjob
        cronjob=l[5]
        #cron expression:
        cronex=l[0:5]
        t=' '.join(str(x) for x in cronex).lstrip('\'')
        jobs[cronjob]=t


#Get execution schedule:
for j,v in jobs.items():
    print("Job:",j,"\t cronex:",v)
    iter = croniter(v, base3)
    print("next at ",iter.get_next(datetime))
    print("then at ",iter.get_next(datetime))
    print("then at ",iter.get_next(datetime))
    print("then at ",iter.get_next(datetime))
    print("then at ",iter.get_next(datetime))
    print()
