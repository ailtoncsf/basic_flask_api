from backend import app
import unittest


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app_test = app.afropython.test_client()
        self.app_test.get('/create')

    def test_get(self):
        self.response = self.app_test.get('/pessoa')
        self.assertEqual(200, self.response.status_code)

    def test_post(self):
        self.response = self.app_test.post('/pessoa', data=dict(nome='Python'))
        self.assertEqual(200, self.response.status_code)
        self.assertIn(b'{"msg":"Pessoa preta adicionada com sucesso!"}', self.response.data)

    def test_put(self):
        self.response = self.app_test.put('/pessoa', data=dict(id='1', nome='Python Edited'))
        self.assertEqual(201, self.response.status_code)
        self.assertIn(b'{"msg":"Nome atualizado com sucesso!"}\n', self.response.data)

    def test_delete(self):
        self.response = self.app_test.delete('/pessoa', data=dict(id='1'))
        self.assertEqual(200, self.response.status_code)

        self.response = self.app_test.get('/pessoa/1')
        self.assertIn(b'[]', self.response.data)
