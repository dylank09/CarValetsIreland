from abc import ABC, abstractmethod


class Factory(ABC):

    @abstractmethod
    def create_user(self, user, colour=None):
        pass

