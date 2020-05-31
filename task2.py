from collections import deque

class CircularBuffer1(object):
    def __init__(self, size, data = []):
        self.index = 0
        self.size = size
        self._data = list(data)[-size:]

    def append(self, value):
        if len(self._data) == self.size:
            self._data[self.index] = value
        else:
            self._data.append(value)
        self.index = (self.index + 1) % self.size

    def __getitem__(self, key):
        if len(self._data) == self.size:
            return(self._data[(key + self.index) % self.size])
        else:
            return(self._data[key])

    def get_all(self):
        return self._data
        
        
class CircularBuffer2(deque):
    def __init__(self, size = 0):
        super().__init__(maxlen=size)
        
