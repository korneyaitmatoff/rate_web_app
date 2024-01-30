from src.services.service import Service
from src.schemas.site import SiteDict, Site
from src.repositories.repository import Repository


class SiteService(Service):
    """Класс-сервис для работы с сущностью "Сайт" """

    def __init__(self, repository: Repository):
        super().__init__(repository=repository)

    def get_sites(self):
        return self.read()

    def get_site_by_id(self, site_id: int) -> Site:
        return self.read(filters=(self.repository.table.id == site_id,))[0]

    def get_sites_by_user_id(self, user_id: int) -> list[Site]:
        return self.read(filters=(self.repository.table.user_id == user_id,))

    def edit_site(self, site_id: int, site: SiteDict):
        self.repository.update(id=site_id, data=dict(site))

        return site_id

    def create_site(self, site: SiteDict) -> Site:
        return self.create(site)

    def delete_site(self, site_id: int):
        self.delete(filters=(self.repository.table.id == site_id,))
