class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, index, element):
        if index < 0 or index > self.size:
            raise IndexError("index out of range")
        new_node = Node(element)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def rotate(self, k):
        if self.size == 0 or k == 0:
            return
        k = k % self.size
        if k == 0:
            return
        new_tail_index = self.size - k - 1
        new_tail = self.head
        for _ in range(new_tail_index):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None

        current = new_head
        while current.next:
            current = current.next
        current.next = self.head
        self.head = new_head

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def append(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def prepend(self, element):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def merge(self, other):
        if self.head is None:
            self.head = other.head
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = other.head
        self.size += other.size

    def interleave(self, other):
        new_list = SinglyLinkedList()
        current1 = self.head
        current2 = other.head
        while current1 or current2:
            if current1:
                new_list.append(current1.value)
                current1 = current1.next
            if current2:
                new_list.append(current2.value)
                current2 = current2.next
        return new_list

    def get_middle_element(self):
        if self.size == 0:
            raise IndexError("Empty list")
        mid_index = self.size // 2
        current = self.head
        for _ in range(mid_index):
            current = current.next
        return current.value

    def index_of(self, element):
        current = self.head
        index = 0
        while current:
            if current.value == element:
                return index
            current = current.next
            index += 1
        return -1

    def split(self, index):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        first_half = SinglyLinkedList()
        second_half = SinglyLinkedList()
        current = self.head
        for i in range(index):
            first_half.append(current.value)
            current = current.next
        while current:
            second_half.append(current.value)
            current = current.next
        return first_half, second_half

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")



