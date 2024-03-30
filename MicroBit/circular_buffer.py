class CircularBuffer:
    def __init__(self, max_size):
        self.data = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def append(self, item):
        self.data[self.head] = item
        self.head = (self.head + 1) % self.max_size
        if self.size < self.max_size:
            self.size += 1
        else:
            self.tail = (self.tail + 1) % self.max_size

    def pop(self):
        if self.is_empty():
            raise IndexError("Buffer is empty")
        item = self.data[self.tail]
        self.tail = (self.tail + 1) % self.max_size
        self.size -= 1
        return item

    def clear(self):
        self.head = 0
        self.tail = 0
        self.size = 0

    def pop_head(self):
        if self.is_empty():
            return None
        item = self.data[self.head - 1]
        self.head = (self.head - 1) % self.max_size
        self.size -= 1
        return item