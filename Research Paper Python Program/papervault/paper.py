from base_entry import LibraryEntry


class ResearchPaper(LibraryEntry):
    def __init__(self, title, authors, year, venue, category="Uncategorized", pdf_name=None):
        super().__init__(title, category)
        self.title = title
        self.authors = authors
        self.year = year
        self.venue = venue
        self.pdf_name = pdf_name
        self.status = "Unread"
        self.notes = []
        self.tags = []
        self.rating = None

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.authors} [{self.category}]"

    def display(self):
        return str(self)
    
    def to_dict(self):
        return {
            "title": self.title,
            "authors": self.authors,
            "year": self.year,
            "venue": self.venue,
            "category": self.category,
            "pdf_name": self.pdf_name,
            "status": self.status
        }
    
    @classmethod
    def from_dict(cls, data):
        paper = cls(
            data["title"],
            data["authors"],
            data["year"],
            data["venue"],
            data.get("category", "Uncategorized"),
            data.get("pdf_name")
        )
        paper.status = data.get("status", "Unread")
        return paper