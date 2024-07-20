from setup import Setup

class SeleniumTest(Setup):
    def abrir(self):
        self.driver.get("https://youtu.be/dQw4w9WgXcQ?si=uqLjhgaF6pHj8CQ1")
        input()
        


if __name__ == "__main__":
    main = SeleniumTest()
    main.abrir()