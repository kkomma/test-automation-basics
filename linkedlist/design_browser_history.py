class BrowserHistory:
    def __init__(self, homepage):
        self.history = [homepage]
        self.current_page = 0

    def visit(self, url):
        # Remove all forward history
        self.history = self.history[:self.current_page + 1]
        self.history.append(url)
        self.current_page += 1

    def back(self, steps):
        self.current_page = max(0, self.current_page - steps)

    def forward(self, steps):
        self.current_page = min(len(self.history) - 1, self.current_page + steps)

    def get_current_page(self):
        return self.history[self.current_page]


def main():
    # Create an instance of BrowserHistory
    browser = BrowserHistory("https://www.google.com")

    # Visit some pages
    browser.visit("https://www.github.com")
    browser.visit("https://www.python.org")
    browser.visit("https://www.stackoverflow.com")

    # Go back 2 steps
    browser.back(2)

    # Go forward 1 step
    browser.forward(1)

    # Get the current page
    current_page = browser.get_current_page()
    print("Current page:", current_page)


if __name__ == "__main__":
    main()