# cron_schedule
Python script to check when cron jobs will run next. Inspired by systemd list-timers and crontab guru

A bit heavy on the libraries but this was the quickest way to get what I needed. Make sure you have all these installed:
```
import subprocess
import os
from croniter import croniter
from datetime import datetime
import dateutil.tz
import io
```
Remember to edit the timezone parameter in the script, to suit your locale.

Recommended: `chmod +x` the file and make an alias to run it (for convenience).

![image](https://user-images.githubusercontent.com/19332617/125656868-2470f92b-3f72-44e1-b465-ca5204d3ed9b.png)
