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
