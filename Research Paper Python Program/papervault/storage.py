import os
import library
import json
from paper import ResearchPaper

class LibraryStorage:

    @staticmethod
    def save_library(library):

        categories = {}

        for paper in library.papers:

            if paper.category not in categories:
                categories[paper.category] = []

            categories[paper.category].append(
                paper.to_dict()
            )

        for category, papers in categories.items():

            folder_path = os.path.join(
                "papers",
                category
            )

            os.makedirs(folder_path, exist_ok=True)

            file_path = os.path.join(
                folder_path,
                "papers.json"
            )

            with open(file_path, "w") as file:
                json.dump(
                    papers,
                    file,
                    indent=4
                )
                
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