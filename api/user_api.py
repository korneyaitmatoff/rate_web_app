from pydantic import StrictInt

from api.api import Api


class UserApi(Api):
    PATH = '/user'

    def __init__(self):
        super().__init__(path=self.PATH)

    def get_user_by_id(self, id: StrictInt):
        return self.get(url=f"{self.url}/{id}").json()
