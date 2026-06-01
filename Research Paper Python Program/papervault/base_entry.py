from abc import ABC, abstractmethod


class LibraryEntry(ABC):
    # Checklist:
    # [ ] Inherit from this base class for any library item.
    def __init__(self, title, category="Uncategorized"):
        self.title = title
        self.category = category

    # Checklist:
    # [ ] Keep each subclass able to serialize itself.
    @abstractmethod
    def to_dict(self):
        pass

    # Checklist:
    # [ ] Keep each subclass able to rebuild itself from saved data.
    @classmethod
    @abstractmethod
    def from_dict(cls, data):
        pass

    # Checklist:
    # [ ] Keep each subclass able to show a simple text view.
    @abstractmethod
    def display(self):
        pass