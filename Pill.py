from datetime import datetime
from datetime import timedelta
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
        return (f"Pill: {self.name} | "
                f"Quantity: {self.quantity} | "
                f"Next Time: {self.nextTime.strftime('%Y-%m-%d %H:%M:%S')} | "
                f"Interval: {self.intervalHours}h")
        
    
