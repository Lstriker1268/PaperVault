class PaperLibrary:
    def __init__(self):
        self.papers = []

    def add_paper(self, paper):
        self.papers.append(paper)

    def view_papers(self):
        if not self.papers:
            print("No papers in library.")
            return

        for index, paper in enumerate(self.papers, start=1):
            print(f"{index}. {paper}")

    def search_by_title(self, keyword):
        results = []

        for paper in self.papers:
            if keyword.lower() in paper.title.lower():
                results.append(paper)

        return results