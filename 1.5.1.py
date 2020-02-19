class MoneyBox:

    def __init__(self, capacity):
        self.capacity = capacity
        self.value = 0

    def can_add(self, v):
        if (self.value + v) <= self.capacity:
            return True
        else:
            return False

    def add(self, v):
        self.value += v


