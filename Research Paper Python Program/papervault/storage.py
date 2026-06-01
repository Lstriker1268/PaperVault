import json
import os
import shutil
import subprocess
from pathlib import Path
from paper import ResearchPaper

class LibraryStorage:
    BASE_DIR = Path(__file__).resolve().parent / "papers"

    @staticmethod
    def _safe_name(value):
        # Make folder and file names safe for Windows paths.
        allowed = []
        for char in value:
            if char.isalnum() or char in (" ", "-", "_"):
                allowed.append(char)
        safe_value = "".join(allowed).strip()
        return safe_value or "untitled"

    @staticmethod
    def _paper_folder(paper):
        return LibraryStorage.BASE_DIR / LibraryStorage._safe_name(paper.category)

    @staticmethod
    def _paper_file_name(paper):
        if paper.pdf_name:
            return paper.pdf_name
        return f"{LibraryStorage._safe_name(paper.title)}.pdf"

    @staticmethod
    def _copy_pdf(source_path, target_path):
        if not source_path:
            return None

        source = Path(source_path)
        if not source.exists():
            return None

        # Save the PDF inside the category folder.
        target_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target_path)
        return target_path.name

    @staticmethod
    def _open_file_or_folder(file_path, folder_path):
        # Try the PDF first, then fall back to the category folder.
        if file_path.exists():
            try:
                os.startfile(file_path)
                return
            except OSError:
                pass

        if folder_path.exists():
            try:
                os.startfile(folder_path)
                return
            except OSError:
                pass

        if file_path.exists():
            subprocess.run(["python", "-m", "webbrowser", str(file_path)], check=False)

    @staticmethod
    def save_library(library, filename):
        data = []

        # Create the main storage directory if it does not exist.
        LibraryStorage.BASE_DIR.mkdir(parents=True, exist_ok=True)

        for paper in library.papers:
            folder = LibraryStorage._paper_folder(paper)
            folder.mkdir(parents=True, exist_ok=True)

            target_file = folder / LibraryStorage._paper_file_name(paper)
            copied_name = LibraryStorage._copy_pdf(getattr(paper, "source_path", None), target_file)
            if copied_name:
                paper.pdf_name = copied_name

            data.append(paper.to_dict())

        with open(filename, "w") as file:
            json.dump(data, file, indent = 4)

    @staticmethod
    def load_library(library, filename, open_files=True):
        try:
            with open(filename, "r") as file:
                data = json.load(file)

            library.papers.clear()

            for paper_data in data:
                paper = ResearchPaper.from_dict(paper_data)
                library.add_paper(paper)

                if open_files:
                    # When loading, try to open the saved PDF automatically.
                    folder = LibraryStorage._paper_folder(paper)
                    file_path = folder / LibraryStorage._paper_file_name(paper)
                    LibraryStorage._open_file_or_folder(file_path, folder)

        except FileNotFoundError:
            print("This. Won't. End. Well. No saved library found.")