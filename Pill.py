from datetime import datetime
from datetime import timedelta
import jdatetime
class Pill:
    def __init__(self,name,intervalHours,quantity):
        self.name = name
        self.intervalHours = intervalHours
        self.quantity = quantity
        self.nextTime = datetime.now() + timedelta(hours=intervalHours)
        

    def takePill(self):
        self.quantity -= 1
        self.nextTime = datetime.now() + timedelta(hours=self.intervalHours)
        
    def __str__(self):
        persian_next = jdatetime.datetime.fromgregorian(datetime=self.nextTime)
        return (f"نام: {self.name} | "
                f"تعداد: {self.quantity} | "
                f"زمان بعدی مصرف: {persian_next.strftime('%Y/%m/%d %H:%M:%S')} | "
                f"هر {self.intervalHours} ساعت")
        
    
