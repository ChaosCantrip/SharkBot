class Permissions:

    def __init__(self, admin: bool):
        self.admin: bool = admin

    @property
    def data(self) -> dict:
        return {
            "admin": self.admin
        }
