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


tracker = TaskTracker()
tracker.add_task("a", "No deadline")
tracker.add_task("b", "Has deadline")
tracker.set_deadline("b", 10)

print(tracker.overdue_pending(10))
print(tracker.overdue_pending(11))

tracker.complete_task("b")
print(tracker.overdue_pending(11))

tracker.rename_task("a", "z")
print(tracker.get_task("z"))
