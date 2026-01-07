from MinHeap import Min_Heap
from Pill import Pill
class ManageSystem:
    def __init__(self):
        self.heap = Min_Heap()
        
    def insert(self,name,intervalHours,quantity):
        pill = Pill(name,intervalHours,quantity)
        self.heap.insert(pill)
        print("added")
    
    def showAll(self):
        return self.heap.printh()