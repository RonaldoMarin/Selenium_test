from time import sleep
from setup import SeleniumSetup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from config import USUARIO, SENHA

class Main(SeleniumSetup):
    
    locator_usuario =           (By.CSS_SELECTOR, '#id_username')
    locator_senha =             (By.CSS_SELECTOR, '#id_password')
    locator_botao_acessar =     (By.CSS_SELECTOR, 'body > div.holder > main > div.flex-container > div.form-login.flex-item > form > div.submit-row > input')

    def abrir_site(self, site):
        return self.driver.get(site)
    
    def autenticar_suap(self):

        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(
            self.locator_usuario
            )
        ).send_keys(USUARIO)

        self.driver.find_element(*self.locator_senha).send_keys(SENHA)
        self.driver.find_element(*self.locator_botao_acessar).click()

        return True

    def verificar_se_autenticou(self):

        url_atual = self.driver.current_url
        try:
            assert url_atual == 'https://suap.ifrn.edu.br/'
            print('Autenticado com sucesso')
        except AssertionError:
            print('Não foi possível autenticar')

if __name__ == '__main__':
    
    main = Main()
    main.abrir_site('https://suap.ifrn.edu.br/accounts/login/?next=/')

    if main.autenticar_suap():
        main.verificar_se_autenticou()

    input('Pressione qualquer tecla para sair:')
    main.driver.quit()