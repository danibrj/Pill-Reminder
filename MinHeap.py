class Min_Heap:
    def __init__(self):
        self.heap = []
        self.n = 0
        
    def insert(self, pill):
        if not self.size():
            self.heap.append(0)
            self.n += 1
            
        self.heap.append(pill)
        self.n += 1
        self._bubble_up(self.n - 1)
    
    def extract_min(self):
        if self.n == 0:
            return -1
        self.heap[1], temp = self.heap[self.n - 1], self.heap[1]
        self.heap.pop()
        self.n -= 1
        self._bubble_down(1)
        return temp
    
    def _bubble_up(self, idx):
        while idx > 1 and self.heap[idx].nextTime < self.heap[idx // 2].nextTime:
            self.heap[idx], self.heap[idx // 2] = self.heap[idx // 2], self.heap[idx]
            idx //= 2
        
    def _bubble_down(self, idx):
        j = 0
        while 2 * idx < self.n and idx != j:
            j = idx
            if self.heap[2 * idx].nextTime < self.heap[j].nextTime:
                j = 2 * idx
            if 2 * idx + 1 < self.n and self.heap[2 * idx + 1].nextTime < self.heap[j].nextTime:
                j = 2 * idx + 1
            self.heap[idx], self.heap[j] = self.heap[j], self.heap[idx]
            idx = j

    def build_heap_with_bubble_down(self, L):
        if len(L) == 0:
            return -1
        self.heap = [0] + L
        self.n = len(self.heap)
        
        for i in range((self.size()- 1) // 2, 0, -1):
            self._bubble_down(i)
            
    def is_empty(self):
        return self.n == 0
    
    def size(self):
        return len(self.heap)
    
    def printh(self):
        for i in self.heap:
            print(i)


# x = Min_Heap()
# x.build_heap_with_bubble_down([5,9,6,1,3])
# x.printh()