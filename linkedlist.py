from node import Node


class LinkedList:
    """Node-based data structure, able to access/manipulate data within the list"""

    def __init__(self):
        """Initializes the front node and length"""

        self._front = None
        self._length = 0

    def length(self):
        """Returns the length of the list"""

        return self._length

    def insert(self, index, entry):
        """Inserts a node at the given index, pushing other nodes back an index"""

        # Check range
        if 0 <= index <= self._length:

            # Create node to be inserted
            new_node = Node(entry)

            # Add to front
            if index == 0:
                new_node.next = self._front
                self._front = new_node
                self._length += 1

            # Add to end
            elif index == self._length:
                jumper = self._front

                # Use a jumper to navigate the end of the list
                for i in range(index-1):
                    jumper = jumper.next

                jumper.next = new_node
                self._length += 1

            # Insert within
            else:
                before_jumper = self._front
                after_jumper = self._front

                # Before jumper will point to the new node
                for i in range(index-1):
                    before_jumper = before_jumper.next

                # The new node will point to the after jumper
                for i in range(index):
                    after_jumper = after_jumper.next

                before_jumper.next = new_node
                new_node.next = after_jumper
                self._length += 1

        # Allows appending but raises an IndexError if out of range
        else:
            raise IndexError()

    def remove(self, index):
        """Removes the entry at the index"""

        pass

    def get_entry(self, index):
        """Returns the node at the given index"""

        if 0 <= index < self._length:
            jumper = self._front

            # Jumper navigates to the node at the given index
            for i in range(index):
                jumper = jumper.next
            return jumper.entry

        # Raise IndexError if out of range
        else:
            raise IndexError()

    def set_entry(self, index, entry):
        """Sets the entry at index, raises a RuntimeError otherwise. Length shouldn't change."""

        pass

    def clear(self):
        """Empties the list"""

        pass
