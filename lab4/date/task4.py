from datetime import datetime

datestr1 = input()
datestr2 = input()
date1 = datetime.strptime(datestr1, "%Y-%d-%m %H:%M:%S")
date2 = datetime.strptime(datestr2, "%Y-%d-%m %H:%M:%S")
res = date2 - date1
ressec = res.total_seconds()
print(ressec)


