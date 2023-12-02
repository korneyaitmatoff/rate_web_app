import requests
from allure import title


@title('Сервис пользователя')
class TestUserService:
    URL: str = 'http://127.0.0.1:8000/site'
    SITE = {"name": 'test', "description": 'test', "url": 'test'}

    @title('Создание сайта')
    def test_create(self):
        assert requests.post(url=self.URL, json=self.SITE).status_code == 200

    @title("Получение сайтов")
    def test_get(self):
        assert requests.get(url=self.URL).status_code == 200

    @title('Удаление сайта')
    def test_delete(self):
        assert requests.put(url=f'{self.URL}/1').status_code == 200
