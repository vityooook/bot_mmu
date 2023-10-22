from datetime import datetime, timedelta

prev_date = datetime.today().date() - timedelta(days=1)
print(prev_date)