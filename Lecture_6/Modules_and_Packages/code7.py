from datetime import datetime, timedelta
now = datetime.now()
future_date = now + timedelta(days=10) # 10 days in the future
past_date = now - timedelta(hours=5) # 5 hours in the past
print("After 10 Days ",future_date)
print("5 hrs before", past_date)
date1 = datetime(2026, 11, 1)
date2 = datetime(2026, 12, 16)
interval = date2 - date1
print(interval) 
