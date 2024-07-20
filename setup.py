from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configurando as opções do Chrome para iniciar maximizado
class Setup():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    # Inicializando o driver do Chrome
    driver = webdriver.Chrome(options=chrome_options)

    # Exemplo de uso: abrindo uma página de exemplo
    # driver.get("https://www.exemplo.com")

    # Seu código Selenium continua aqui...

    # Fechar o navegador ao finalizar o script
    # driver.quit()

# class SeleniumTest(Setup):
#     def abrir(self):
#         Setup.driver.get("https://github.com/RonaldoMarin/Selenium_test")
#         input()

# if __name__ == "__main__":
#     main = SeleniumTest()
#     main.abrir()