"""
Program Name: Word Count Analyzer
Author: Liam Malone
Purpose: This program lets the user select one of four text files and counts how often each word appears.
Starter Code: No starter code was used.
Date: July 8, 2026
"""

from pathlib import Path
import string


class WordAnalyzer:
    """A class that analyzes a text file and counts word frequencies."""

    def __init__(self, filepath):
        self._filepath = Path(filepath)
        self._frequencies = {}

    def process_file(self):
        """Read the file, clean the words, and count each word."""
        try:
            if not self._filepath.exists():
                raise FileNotFoundError

            self._frequencies = {}

            punctuation_table = str.maketrans("", "", string.punctuation)

            with self._filepath.open("r", encoding="utf-8") as file:
                for line in file:
                    line = line.translate(punctuation_table)
                    line = line.lower()
                    words = line.split()

                    for word in words:
                        if word in self._frequencies:
                            self._frequencies[word] += 1
                        else:
                            self._frequencies[word] = 1

            return True

        except FileNotFoundError:
            print(f"Error: The file '{self._filepath.name}' was not found.")
            return False

    def print_report(self):
        """Print the word count report in alphabetical order."""
        sorted_words = sorted(self._frequencies.keys())

        for word in sorted_words:
            print(f"{word:<15} :: {self._frequencies[word]}")


def main():
    """Display the file menu and run the word analyzer."""
    base_path = Path(__file__).parent

    file_choices = {
        "1": base_path / "princess_mars.txt",
        "2": base_path / "Tarzan.txt",
        "3": base_path / "treasure_island.txt",
        "4": base_path / "monte_cristo.txt"
    }

    while True:
        print()
        print("--- Word Analyzer ---")
        print("Please select a file to analyze:")

        for choice, file_path in file_choices.items():
            file_name = file_path.stem.replace("_", " ").title()
            print(f"{choice}. {file_name}")

        print("5. Exit")
        print()

        user_choice = input("Enter your choice (1-5): ")

        if user_choice == "5":
            print()
            print("Goodbye!")
            break

        elif user_choice in file_choices:
            selected_file = file_choices[user_choice]

            print()
            print(f"Processing '{selected_file.name}'...")
            print()

            analyzer = WordAnalyzer(str(selected_file))

            if analyzer.process_file():
                analyzer.print_report()

        else:
            print()
            print("Invalid choice. Please select from 1-5.")

        print()
        input("Press Enter to return to the menu...")


if __name__ == "__main__":
    main()