class ResearchPaper:
    def __init__(self, title, authors, year, venue):
        self.title = title
        self.authors = authors
        self.year = year
        self.venue = venue
        self.status = "Unread"
        self.notes = []
        self.tags = []
        self.rating = None

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.authors}"
    
    def to_dict(self):
        return {
            "title": self.title,
            "authors": self.authors,
            "year": self.year,
            "venue": self.venue,
            "status": self.status
        }
    
    @classmethod
    def from_dict(cls, data):
        paper = cls(
            data["title"],
            data["authors"],
            data["year"],
            data["venue"]
        )
        paper.status = data["status"]
        return paper