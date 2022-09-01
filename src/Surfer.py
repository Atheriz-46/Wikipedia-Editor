class Surfer:
    """
    Used to maintain the pages that have been visited in a stack to facilitate the "back" button
    """
    stack = []

    def currentTop(self):
        """
        Used to find the last visited page (topmost page in the stack). Returns the home page if the stack is empty

        """

        if len(self.stack) == 0:
            return "HomePage.md"
        else:
            return self.stack[-1]

    def back(self):
        """
        Returns to the previously visited page. Pops the topmost page in the stack if any and returns the subsequent topmost page
        """

        if len(self.stack) > 0:
            self.stack.pop()
        return self.currentTop()

    def push(self, x):
        """
        Used to add a page to the stack. Called when a new page is opened.

        Args:
            x (str) : Refers to the filename / page that has been visited and is to be pushed to the stack
        """

        self.stack.append(x)
