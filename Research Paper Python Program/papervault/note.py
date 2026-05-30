from datetime import datetime

class Note:
    def __init__(self, content, category = "general"):
        self.content = content
        self.category = category
        self.created_at = datetime.now()

    def __str__(self):
        return f"[{self.category}] {self.content}"