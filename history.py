from linkedlist import LinkedList


class History:
    """A class that mimics the behavior of a web browser's back button, forward button, and address bar"""

    def __init__(self):
        self.browser_history = LinkedList()
        self.place = -1

    def navigate_to(self, url):
        """The browser navigates to the given url"""

        # Insert a URL after the set place
        self.browser_history.insert(self.place+1, url)
        self.place += 1

    def forward(self):
        """If possible, the browser navigates forward in the history, otherwise it stays in place"""

        pass

    def back(self):
        """If possible, the browser navigates backwards in the history, otherwise it stays in place"""

        pass

    def history(self):
        """Returns a well formatted string with the current history"""

        content = "Oldest\n===========\n"
        for i in range(self.browser_history.length()):
            if self.place == i:
                content += self.browser_history.get_entry(i) + "\t<==current\n"
            else:
                content += self.browser_history.get_entry(i) + "\n"
        content += "===========\nNewest\n"
        return content
