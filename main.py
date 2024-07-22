from setup import Setup
from selenium.webdriver.common.by import By
from time import sleep


class SeleniumTest(Setup):

    input_login_suap = (By.NAME, 'username')
    input_senha_suap = (By.NAME, 'password')
    botao_acessar_suap = (By.CLASS_NAME, 'submit-row')
    botao_ensino_suap = (By.CLASS_NAME, 'menu-ensino')
    botao_boletins_suap = (By.CSS_SELECTOR, '#menu-item-ensino_boletins > a')
    botao_documentos_suap = (By.CSS_SELECTOR, '#content > div.title-container > div.action-bar-container > ul > li:nth-child(2) > a')
    botao_declaracao_de_vinculo = (By.CSS_SELECTOR, '#content > div.title-container > div.action-bar-container > ul > li:nth-child(2) > ul > li:nth-child(1) > a')


    def abrir(self):
        self.driver.get("https://suap.ifrn.edu.br/accounts/login/?next=/")

    def logar_no_suap(self):
        login = "20211014040044"
        self.driver.find_element(*self.input_login_suap).send_keys(login)
        self.driver.find_element(*self.input_senha_suap)
        input()
        self.driver.find_element(*self.botao_acessar_suap).click()
        print(1)

    def navegar_ate_aba_boletim(self):
        self.driver.find_element(*self.botao_ensino_suap).click()
        sleep(0.3)
        self.driver.find_element(*self.botao_boletins_suap).click()
        sleep(2)


if __name__ == "__main__":
    main = SeleniumTest()
    main.abrir()
    main.logar_no_suap()
    main.navegar_ate_aba_boletim()