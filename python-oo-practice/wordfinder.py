"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Machine for finding random words from dictionary

    >>> wf = wordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """

    def __init__(self, path):
        """Read dictionary and reports # items read."""

        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")
    
    def parse(self, dict_file):
        """PArse dict_file -> list of words"""

        return [w.strip() for w in dict_file]
    
    def random(self):
        return random.choice(self.words)
    
    class specialWordFinder(WordFinder):
        """Specialzed WordFiner that exludes blank lines/comments

        >>> swf = SpecialWordFiner("complex.txt")
        3 words read

        >>> swf.random() in ["pear", "carrot", "kale"]
        True

        >>> swf.random() in ["pear", "carrot", "kale"]
        True

        >>> swf.random() in ["pear", "carrot", "kale"]
        True
        """

        def parse(self, dict_file):
            """Parse dict_file -> list of words, skipping blanks/comments"""

            return [w.strip() for w in dict_file
                    if w.strip() and not w.startswith("#")]