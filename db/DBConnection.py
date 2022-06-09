from abc import ABCMeta, abstractmethod


class DBConnection(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get(self, key: str) -> str:
        pass

    @abstractmethod
    def put(self, key: str, value: str) -> None:
        pass

    @abstractmethod
    def delete(self, key: str) -> None:
        pass