from abc import abstractmethod


class Observer():

    def __init__(self):
        self._subject = None

    @abstractmethod
    def update(self, subject):
        pass
    