from linkedlist import LinkedList


class History:
    """A class that mimics the behavior of a web browser's back button, forward button, and address bar"""

    def __init__(self):
        """Initializes an empty linked list and sets the initial position to nonexistent"""

        self.browser_history = LinkedList()
        self._place = -1

    def navigate_to(self, url):
        """The browser navigates to the given url"""

        # Insert a URL after the set place
        self.browser_history.insert(self._place+1, url)
        self._place += 1

        # Remove all URLs past the inserted point
        while self.browser_history.length() > self._place + 1:
            self.browser_history.remove(self._place + 1)

    def forward(self):
        """If possible, the browser navigates forward in the history, otherwise it stays in place"""

        # Stay in place if there's nothing past the current position
        if self._place < self.browser_history.length() - 1:
            self._place += 1

    def back(self):
        """If possible, the browser navigates backwards in the history, otherwise it stays in place"""

        # Stay in place if there's nothing before the current position
        if self._place > 0:
            self._place -= 1

    def history(self):
        """Returns a well formatted string with the current history"""

        content = "Oldest\n===========\n"
        
        # Add every URL
        for i in range(self.browser_history.length()):

            # Place current pointer at appropriate URL
            if self._place == i:
                content += self.browser_history.get_entry(i) + "\t<==current\n"
            else:
                content += self.browser_history.get_entry(i) + "\n"

        # Finalize the content printed out
        content += "===========\nNewest\n"
        
        return content
