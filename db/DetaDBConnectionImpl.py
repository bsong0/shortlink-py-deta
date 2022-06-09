import deta

import config
import db.DBConnection
from deta import Deta

class DetaDBConnectionImpl(db.DBConnection.DBConnection):

    def __init__(self) -> None:
        self.deta = Deta(config.DetaConfig.PROJECT_KEY)
        self.db = self.deta.Base(config.DetaConfig.BASE_NAME)

    def get(self, key: str) -> str:
        return self.db.get(key)

    def put(self, key: str, value: str) -> None:
        self.db.put(value, key)

    def delete(self, key: str) -> None:
        self.db.delete(key)