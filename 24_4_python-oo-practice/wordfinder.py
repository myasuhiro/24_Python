"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Finding random words from dictionaly.
    """

    def __init__(self, path):
        """Read dictionary"""
        
        dict_file = open(path)

        self.words = [w.strip() for w in dict_file]

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Change dict_file to List of words."""

        return [w.strip() for w in dict_file]
    
    def random(self):
        """Return random word."""

        return random.choice((self.words))
    
class SpecialWordFinder(WordFinder):
    """Finding random words from dictionary without blank lines/comments"""

    def parse(self, dict_file):
        return [w.strip() for w in dict_file if w.strip() and not w.startwith("#")]