from collections import deque


class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, val: int):
        self.balance += val

    def get_balance(self):
        return self.balance


ba = BankAccount()
ba.deposit(100)
print(ba.get_balance())
ba.deposit(23)
print(ba.get_balance())


class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()  # initialize an empty queue
        self.total = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.total += val
        if len(self.queue) > self.size:
            takeaway = self.queue.popleft()
            self.total -= takeaway
        return self.total / len(self.queue)
