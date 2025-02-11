from datetime import datetime
date1=datetime(2025,2,11,14,30,0)
date2=datetime(2025,2,10,12,15,0)
diff=abs((date2-date1).total_seconds())
print(int(diff))