from datetime import datetime, timedelta
today=datetime.today()
days_before=today-timedelta(days=5)
print(days_before)