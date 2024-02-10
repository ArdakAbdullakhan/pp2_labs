from datetime import datetime, timedelta

x = datetime.now()
res = x - timedelta(days=1)
y = res.strftime("%Y-%m-%d")
print(y)
res = x + timedelta(days=1)
t = res.strftime("%Y-%m-%d")
print(t)

