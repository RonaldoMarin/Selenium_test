import selenium
from time import sleep
import undetected_chromedriver as uc

class SeleniumSetup:

    options = uc.ChromeOptions()
    options.headless = False
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")

    driver = uc.Chrome(options = options, version_main=126)



