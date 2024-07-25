# test_system.py
import unittest
import requests

class TestSystem(unittest.TestCase):
    BASE_URL = 'http://127.0.0.1:5000'

    def test_system(self):
        # Testa se o endpoint de usuários retorna a lista correta
        response = requests.get(f'{self.BASE_URL}/users')
        self.assertEqual(response.status_code, 200)
        users = response.json()
        self.assertEqual(len(users), 2)

        # Testa se o endpoint de usuário específico retorna o usuário correto
        response = requests.get(f'{self.BASE_URL}/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], 'Alice')

        # Testa se o endpoint de usuário específico retorna erro para ID não existente
        response = requests.get(f'{self.BASE_URL}/users/3')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
