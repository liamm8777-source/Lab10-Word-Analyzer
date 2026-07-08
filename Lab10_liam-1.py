"""
Program Name: Word Count Analyzer
Author: Liam Malone
Purpose: This program lets the user select one of four text files and counts how often each word appears.
Starter Code: No starter code was used.
Date: July 8, 2026
"""

from pathlib import Path
import string


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
            print(f"Error: The file '{self._filepath}' was not found.")
            return False

    def print_report(self):
        """Print the word count report in alphabetical order."""
        sorted_words = sorted(self._frequencies.keys())

        for word in sorted_words:
            print(f"{word:<15} :: {self._frequencies[word]}")