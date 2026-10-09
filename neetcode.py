import random


class Neet:
    def __init__(self):
        self.values = {}
        self.list = []

    def insert_value(self, val: int) -> bool:
        if val is None:
            return False
        if val not in self.values:
            self.values[val] = set()
        self.values[val].add(len(self.values))
        self.list.append(val)
        return True

    def remove_value(self, val: int) -> bool:
        if val not in self.values:
            return False
        pop_index = self.values[val].pop()
        list_len = len(self.list)
        [self.list[pop_index], self.list[list_len - 1]
         ] = [self.list[list_len - 1], self.list[pop_index]]
        self.values[self.list[pop_index]] = pop_index
        self.list.pop()
        del self.values[val]  # O(1)
        return True

    def get_random(self) -> int:
        return random.choice(self.list)


values = Neet()
values.insert_value(5)
values.insert_value(-10)
values.insert_value(2)
values.insert_value(6)
values.insert_value(0)
print(values.get_random())
