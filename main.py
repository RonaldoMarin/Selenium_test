from time import sleep
from setup import Setup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class SeleniumTest(Setup):

    input_login_github = (By.ID, 'login_field')
    botao_login_github = (By.CSS_SELECTOR, '#login > div.auth-form-body.mt-3 > form > div > input.btn.btn-primary.btn-block.js-sign-in-button')
    botao_new_github = (By.CSS_SELECTOR, 'body > div.logged-in.env-production.page-responsive.full-width > div.application-main > div > div > aside > div > div > loading-context > div > div.Details.js-repos-container > div > div.hide-sm.hide-md.mb-1.d-flex.flex-justify-between.flex-items-center > a')
    input_repository_name_github = (By.CSS_SELECTOR, '#\:rb\:')
    botao_criar_repositorio_github = (By.XPATH, '/html/body/div[1]/div[5]/main/react-app/div/form/div[4]/div[1]/div[1]/div[1]/fieldset/div/div[2]/div/span/input')


    def abrir(self):
        self.driver.get("https://github.com/login")

    def logar_no_github(self):
        login = "ronaldoMarin"
        self.driver.find_element(*self.input_login_github).send_keys(login)
        input()
        self.driver.find_element(*self.botao_login_github).click()
        print(1)

    def criar_repositorio(self, nome_repositorio:str):
        self.driver.find_element(*self.botao_new_github).click()
        sleep(0.3)

        # WAITS
        WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable((By.ID, ':r7:'))
        ).send_keys(nome_repositorio)

        self.driver.find_element(*self.botao_criar_repositorio_github).click()
        sleep(2)


if __name__ == "__main__":
    main = SeleniumTest()
    main.abrir()
    main.logar_no_github()
    nome_repositorio = "TESTE_E_LEGAL"
    main.criar_repositorio(nome_repositorio)
    input()