class DynamicArray:
    def __init__(self, initial_capacity=2, resize_factor=2):
        self.capacity = initial_capacity
        self.size = 0
        self.resize_factor = resize_factor
        self.data = [0] * self.capacity

    def resize(self, new_capacity):
        new_data = [0] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def insert(self, index, element):
        if index < 0 or index > self.size:
            raise IndexError("index out of range")
        if self.size == self.capacity:
            self.resize(self.capacity * self.resize_factor)
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = element
        self.size += 1

    def erase(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.size -= 1
        if self.size < self.capacity // self.resize_factor:
            self.resize(self.capacity // self.resize_factor)

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def rotate(self, k):
        if self.size == 0:
            return
        k = k % self.size
        self.data[:self.size] = self.data[:self.size][::-1]
        self.data[:k] = self.data[:k][::-1]
        self.data[k:self.size] = self.data[k:self.size][::-1]

    def reverse(self):
        self.data[:self.size] = self.data[:self.size][::-1]

    def append(self, element):
        if self.size == self.capacity:
            self.resize(self.capacity * self.resize_factor)
        self.data[self.size] = element
        self.size += 1

    def prepend(self, element):
        self.insert(0, element)

    def merge(self, other):
        for i in range(other.size):
            self.append(other.data[i])

    def interleave(self, other):
        new_array = DynamicArray()
        i, j = 0, 0
        while i < self.size or j < other.size:
            if i < self.size:
                new_array.append(self.data[i])
                i += 1
            if j < other.size:
                new_array.append(other.data[j])
                j += 1
        return new_array

    def get_middle_element(self):
        if self.size == 0:
            raise IndexError("Empty array")
        return self.data[self.size // 2]

    def index_of(self, element):
        for i in range(self.size):
            if self.data[i] == element:
                return i
        return -1

    def split(self, index):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        first_half = DynamicArray()
        second_half = DynamicArray()
        for i in range(index):
            first_half.append(self.data[i])
        for i in range(index, self.size):
            second_half.append(self.data[i])
        return first_half, second_half

    def print(self):
        print(" ".join(map(str, self.data[:self.size])))


