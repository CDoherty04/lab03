from linkedlist import LinkedList


class History:
    """A class that mimics the behavior of a web browser's back button, forward button, and address bar"""

    def __init__(self):
        self.browser_history = LinkedList()

    def navigate_to(self, url):
        """The browser navigates to the given url"""

        pass

    def forward(self):
        """If possible, the browser navigates forward in the history, otherwise it stays in place"""

        pass

    def back(self):
        """If possible, the browser navigates backwards in the history, otherwise it stays in place"""

        pass

    def history(self):
        """Returns a well formatted string with the current history"""

        pass
