from datetime import datetime, timedelta

x = datetime.now()
res = x - timedelta(days=5)
frmres = res.strftime("%Y-%m-%d")

print(frmres)
