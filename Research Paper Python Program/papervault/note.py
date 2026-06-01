from datetime import datetime
from base_entry import LibraryEntry


class Note(LibraryEntry):
    def __init__(self, content, category = "general"):
        super().__init__(content, category)
        self.content = content
        self.created_at = datetime.now()

    def __str__(self):
        return f"[{self.category}] {self.content}"

    def display(self):
        return str(self)

    def to_dict(self):
        return {
            "content": self.content,
            "category": self.category,
            "created_at": self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        note = cls(data["content"], data.get("category", "general"))
        return note