import json
from paper import ResearchPaper

class LibraryStorage:

    @staticmethod
    def save_library(library, filename):
        data = []

    for paper in library.papers:
        data.append(paper.to_dict())

    with open(filename, "w") as file:
        json.dump(data, file, indent = 4)

    @staticmethod
    def load_library(library, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)

            library.papers.clear()

            for paper_data in data:
                paper = ResearchPaper.from_dict(paper_data)
                library.add_paper(paper)

        except FileNotFoundError:
            print("This. Won't. End. Well. No saved library found.")