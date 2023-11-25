import requests
from allure import title


@title('Сервис пользователя')
class TestUserService:
    URL: str = 'http://127.0.0.1:8000/user'
    USER = {"name": 'test', "login": 'test', "password": 'test'}

    @title('Создание пользователя')
    def test_create(self):
        assert requests.post(url=self.URL, json=self.USER).status_code == 200

    @title("Получение пользователей")
    def test_get(self):
        assert requests.get(url=self.URL).status_code == 200

    @title('Удаление пользователя')
    def test_delete(self):
        assert requests.put(url=f'{self.URL}/1').status_code == 200
