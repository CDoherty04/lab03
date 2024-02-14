class Node:
    """The building blocks for linked data structures"""

    def __init__(self, entry):
        """Holds a value, entry, and points to another node"""

        self.entry = entry
        self.next = None
