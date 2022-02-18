from abc import abstractmethod


class Item():
    @abstractmethod
    def accept(self):
        pass
