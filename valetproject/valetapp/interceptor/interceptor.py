from abc import abstractmethod


class interceptor:
    def __init__(self) -> None:
        pass

    @abstractmethod
    def log(self):
        pass
