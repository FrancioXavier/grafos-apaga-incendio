class BinaryHeap:
    def __init__(self, is_min_heap=True):
        self.heap = []
        self.is_min_heap = is_min_heap
        
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def has_parent(self, i):
        return self.parent(i) >= 0
    
    def has_left_child(self, i):
        return self.left_child(i) < len(self.heap)
    
    def has_right_child(self, i):
        return self.right_child(i) < len(self.heap)
    
    def compare(self, a, b):
        if self.is_min_heap:
            return a < b  # Min-heap
        return a > b  # Max-heap
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]
    
    def push(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)
    
    def pop(self):
        if not self.heap:
            return None
        
        root = self.heap[0]
        last_element = self.heap.pop()
        
        if self.heap:  # Se ainda há elementos após o pop
            self.heap[0] = last_element
            self._sift_down(0)
        
        return root
    
    def _sift_up(self, i):
        while self.has_parent(i) and self.compare(self.heap[i], self.heap[self.parent(i)]):
            self.swap(i, self.parent(i))
            i = self.parent(i)
    
    def _sift_down(self, i):
        smallest_or_largest = i
        
        if (self.has_left_child(i) and 
                self.compare(self.heap[self.left_child(i)], self.heap[smallest_or_largest])):
            smallest_or_largest = self.left_child(i)
        
        if (self.has_right_child(i) and 
                self.compare(self.heap[self.right_child(i)], self.heap[smallest_or_largest])):
            smallest_or_largest = self.right_child(i)
        
        if i != smallest_or_largest:
            self.swap(i, smallest_or_largest)
            self._sift_down(smallest_or_largest)