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