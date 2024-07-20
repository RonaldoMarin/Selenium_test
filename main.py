from setup import Setup

class SeleniumTest(Setup):
    def abrir(self):
        self.driver.get("https://github.com/RonaldoMarin/Selenium_test")
        input()
        


if __name__ == "__main__":
    main = SeleniumTest()
    main.abrir()