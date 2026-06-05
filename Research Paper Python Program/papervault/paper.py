class ResearchPaper:
    def __init__(
        self,
        title,
        authors,
        year,
        venue,
        category="General",
        pdf_path=""
    ):
        self.title = title
        self.authors = authors
        self.year = year
        self.venue = venue
        self.category = category
        self.pdf_path = pdf_path

        self.status = "Unread"
        self.notes = []
        self.tags = []
        self.rating = None

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.authors} [{self.category}]"
    
    def to_dict(self):
        return {
            "title": self.title,
            "authors": self.authors,
            "year": self.year,
            "venue": self.venue,
            "category": self.category,
            "pdf_path": self.pdf_path,
            "status": self.status
        }
    
    @classmethod
    def from_dict(cls, data):
        paper = cls(
            data["title"],
            data["authors"],
            data["year"],
            data["venue"],
            data.get("category", "General"),
            data.get("pdf_path", "")
        )
        paper.status = data["status"]
        return paper