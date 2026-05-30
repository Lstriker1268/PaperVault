from library import PaperLibrary
from paper import ResearchPaper
from storage import LibraryStorage

library = PaperLibrary()

while True:
    print("\n=== PaperVault ===")
    print("1. Add paper")
    print("2. View papers")
    print("3. Search papers")
    print("4. Save library")
    print("5. Load library")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Title: ")
        authors = input("Authors: ")
        year = int(input("Year: "))
        venue = input("Venue: ")

        paper = ResearchPaper(title, authors, year, venue)

        library.add_paper(paper)

        print("Paper added successfully!")

    elif choice == "2":
        library.view_papers()

    elif choice == "3":
        keyword = input("Enter title keyword: ")

        results = library.search_by_title(keyword)

        if results:
            print("\nResults:")
            for paper in results:
                print(paper)

        else:
            print("Uh oh! No papers found!")

    elif choice == "4":
        LibraryStorage.save_library(
            library,
            "papers.json"
        )
        print("Everything has a beginning. Library saved.")

    elif choice == "5":
        LibraryStorage.load_library(
            library,
            "papers.json"
        )
        print("To master your blade, you must first control your emotions. Library loaded.")

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")