from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Setup():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    # Inicializando o driver do Chrome
    driver = webdriver.Chrome(options=chrome_options)

    