class Notebook:
    def __init__(self):
        self.notes = {}
        self.history = []

    def add_note(self, title: str, text: str) -> bool:
        if title in self.notes:
            return False
        self.history.append(("add", title))
        self.notes[title] = text
        return True

    def get_note(self, title: str) -> str | None:
        # Your code here
        if title in self.notes:
            return self.notes[title]
        return None

    def delete_note(self, title: str) -> bool:
        if title in self.notes:
            self.history.append(("delete", title, self.notes[title]))
            del self.notes[title]
            return True
        return False

    def rename_note(self, old_title: str, new_title: str) -> bool:
        if new_title in self.notes or old_title not in self.notes:
            return False
        self.history.append(("rename", old_title, new_title))
        self.notes[new_title] = self.notes[old_title]
        del self.notes[old_title]
        return True

    def list_titles(self, prefix: str) -> list[str]:
        titles = []
        for title in self.notes:
            if title.startswith(prefix):
                titles.append(title)
        titles.sort()
        return titles

    def update_note(self, title: str, text: str) -> bool:
        if title in self.notes:
            self.history.append(("update", title, self.notes[title]))
            self.notes[title] = text
            return True
        return False

    def search_notes(self, query: str) -> list[str]:
        titles = []
        for title, note in self.notes.items():
            if note.find(query) != -1:
                titles.append(title)
        titles.sort()
        return titles

    def undo(self) -> bool:
        if self.history:
            undo = self.history.pop()
            if undo[0] == "add":
                del self.notes[undo[1]]
            elif undo[0] == "update" or undo[0] == "delete":
                self.notes[undo[1]] = undo[2]
            elif undo[0] == "rename":
                self.notes[undo[2]] = self.notes[undo[1]]
                del self.notes[undo[1]]
            return True
        return False


class TaskTracker:
    def __init__(self):
        self.tasks = {}
        self.pending = set()
        self.priorities = {}
        self.deadlines = {}

    def add_task(self, task_id: str, description: str) -> bool:
        if task_id in self.tasks:
            return False
        self.tasks[task_id] = description
        self.pending.add(task_id)
        self.priorities[task_id] = 0
        return True

    def complete_task(self, task_id: str) -> bool:
        if task_id not in self.tasks or task_id not in self.pending:
            return False
        self.pending.remove(task_id)
        return True

    def get_task(self, task_id: str) -> tuple[str, bool] | None:
        if task_id not in self.tasks:
            return None

        return (self.tasks[task_id], task_id not in self.pending)

    def list_pending(self) -> list[str]:
        return sorted(self.pending)

    def reopen_task(self, task_id: str) -> bool:
        if task_id not in self.tasks or task_id in self.pending:
            return False
        self.pending.add(task_id)
        return True

    def rename_task(self, old_id: str, new_id: str) -> bool:
        if old_id not in self.tasks or new_id in self.tasks:
            return False
        self.tasks[new_id] = self.tasks[old_id]
        if old_id in self.pending:
            self.pending.add(new_id)
            self.pending.remove(old_id)
        if old_id in self.deadlines:
            self.deadlines[new_id] = self.deadlines[old_id]
            del self.deadlines[old_id]
        self.priorities[new_id] = self.priorities[old_id]
        del self.priorities[old_id]
        del self.tasks[old_id]
        return True

    def set_priority(self, task_id: str, priority: int) -> bool:
        if task_id not in self.tasks:
            return False
        self.priorities[task_id] = priority
        return True

    def top_pending(self, limit: int) -> list[str]:
        if limit <= 0:
            return []
        t_pending = sorted(self.pending,
                           key=lambda task_id: (-self.priorities[task_id], task_id))
        return t_pending[:limit]

    def search_pending(self, query: str, limit: int) -> list[str]:
        if limit <= 0:
            return []
        inn = []
        for task in self.pending:
            if query in self.tasks[task]:
                inn.append(task)
        return sorted(inn, key=lambda task: (-self.priorities[task], task))[:limit]

    def set_deadline(self, task_id: str, deadline: int) -> bool:
        if task_id not in self.tasks:
            return False
        self.deadlines[task_id] = deadline
        return True

    def overdue_pending(self, now: int) -> list[str]:
        pending = []
        for task, deadline in self.deadlines.items():
            if task in self.pending and deadline < now:
                pending.append(task)
        return sorted(pending, key=lambda task: (self.deadlines[task], task))

    def delete_task(self, task_id: str) -> bool:
        if task_id not in self.tasks:
            return False

        del self.tasks[task_id]
        del self.priorities[task_id]
        if task_id in self.pending:
            self.pending.remove(task_id)
        if task_id in self.deadlines:
            del self.deadlines[task_id]
        return True


# tracker = TaskTracker()
# tracker.add_task("a", "Original")
# tracker.set_priority("a", 9)
# tracker.set_deadline("a", 10)
# tracker.complete_task("a")

# assert tracker.delete_task("a") is True
# assert tracker.delete_task("a") is False
# assert tracker.get_task("a") is None

# assert tracker.add_task("a", "Fresh") is True
# assert tracker.get_task("a") == ("Fresh", False)
# assert tracker.priorities["a"] == 0
# assert tracker.overdue_pending(100) == []
# assert tracker.list_pending() == ["a"]


"""
Rules:
Level 1
- add_item: Return False if the ID exists or quantity is negative. Otherwise create the item and return True. Zero is valid.
- get_quantity: Return the quantity, or None if missing.
- change_quantity: Add delta to the current quantity. Return False if the ID is missing or the resulting quantity would be negative; otherwise return True. A zero delta succeeds for an existing item.
- remove_item: Remove an existing item and return True; return False if missing.
- Failed operations leave state unchanged.
- Separate instances have separate inventory.
Level 2
- list_items: Return IDs starting with prefix, alphabetically sorted. An empty prefix matches all IDs.
- lowest_stock: Return at most limit IDs ordered by quantity ascending, then ID alphabetically. Include zero-stock items. Return [] for limit <= 0.
transfer: Move amount units from source to destination. Return False if either ID is missing, IDs are identical, amount is nonpositive, or source stock is insufficient. Otherwise return True.
- Failed operations leave state unchanged.
"""


class Inventory:
    def __init__(self):
        self.items = {}
        self.reservations = {}
        self.available = {}

    def add_item(self, item_id: str, quantity: int) -> bool:
        if item_id in self.items or quantity < 0:
            return False
        self.items[item_id] = quantity
        self.available[item_id] = quantity
        return True

    def get_quantity(self, item_id: str) -> int | None:
        return self.items[item_id] if item_id in self.items else None

    def change_quantity(self, item_id: str, delta: int) -> bool:
        if item_id not in self.items or self.available[item_id] + delta < 0:
            return False
        self.items[item_id] += delta
        self.available[item_id] += delta
        return True

    def remove_item(self, item_id: str) -> bool:
        if item_id in self.items and self.available[item_id] == self.items[item_id]:
            del self.items[item_id]
            del self.available[item_id]
            return True
        return False

    def list_items(self, prefix: str) -> list[str]:
        matching = []
        for item in self.items.keys():
            if item.startswith(prefix):
                matching.append(item)
        return sorted(matching)

    def lowest_stock(self, limit: int) -> list[str]:
        if limit < 0:
            return []

        return sorted(self.items, key=lambda item: (self.items[item], item))[:limit]

    def transfer(self, source_id: str, destination_id: str, amount: int) -> bool:
        if source_id not in self.items or destination_id not in self.items or source_id == destination_id or amount <= 0 or self.items[source_id] < amount or self.available[source_id] < amount:
            return False
        self.items[source_id] -= amount
        self.items[destination_id] += amount
        self.available[source_id] -= amount
        self.available[destination_id] += amount
        return True

    def reserve(self, reservation_id: str, item_id: str, amount: int) -> bool:
        if reservation_id in self.reservations or item_id not in self.items or amount > self.items[item_id] or amount <= 0 or self.available[item_id] < amount:
            return False
        self.reservations[reservation_id] = (item_id, amount)
        self.available[item_id] -= amount
        return True

    def cancel_reservation(self, reservation_id: str) -> bool:
        if reservation_id not in self.reservations:
            return False
        item_id, amount = self.reservations[reservation_id]
        self.available[item_id] += amount
        del self.reservations[reservation_id]
        return True

    def fulfill_reservation(self, reservation_id: str) -> bool:
        if reservation_id not in self.reservations:
            return False
        item_id, amount = self.reservations[reservation_id]
        self.items[item_id] -= amount
        del self.reservations[reservation_id]
        return True

    def get_available(self, item_id: str) -> int | None:
        if item_id not in self.items:
            return None
        return self.available[item_id]

    def rename_item(self, old_id: str, new_id: str) -> bool:
        if old_id not in self.items or new_id in self.items:
            return False
        for res, item in self.reservations.items():  # {str: tuple(str, int)}
            if item[0] == old_id:
                self.reservations[res] = (new_id, item[1])
        self.available[new_id] = self.available[old_id]
        del self.available[old_id]
        self.items[new_id] = self.items[old_id]
        del self.items[old_id]
        return True

        # Tests
        # inventory = Inventory()


        # print(inventory.add_item("pens", 5))           # True
        # print(inventory.add_item("pens", 2))           # False
        # print(inventory.change_quantity("pens", -6))  # False
        # print(inventory.get_quantity("pens"))         # 5
        # print(inventory.change_quantity("pens", -5))  # True
        # print(inventory.get_quantity("pens"))         # 0
        # print(inventory.remove_item("pens"))          # True
        # print(inventory.get_quantity("pens"))         # None
        # print(inventory.add_item("pens", 5))
        # print(inventory.add_item("paper", 2))
        # print(inventory.add_item("clips", 2))
        # print(inventory.list_items("pa"))             # ["paper"]
        # print(inventory.lowest_stock(2))              # ["clips", "paper"]
        # print(inventory.transfer("pens", "paper", 3))  # True
        # print(inventory.get_quantity("pens"))         # 2
        # print(inventory.get_quantity("paper"))        # 5
        # print(inventory.transfer("pens", "paper", 3))  # False
inventory = Inventory()
inventory.add_item("pens", 10)
inventory.reserve("r1", "pens", 3)
inventory.reserve("r2", "pens", 2)

assert inventory.rename_item("pens", "markers")
assert inventory.get_quantity("pens") is None
assert inventory.get_quantity("markers") == 10
assert inventory.get_available("markers") == 5

assert inventory.cancel_reservation("r1")
assert inventory.get_available("markers") == 8

assert inventory.fulfill_reservation("r2")
assert inventory.get_quantity("markers") == 8
assert inventory.get_available("markers") == 8
