from abc import abstractmethod


class interceptor:
    def __init__(self) -> None:
        pass

    @abstractmethod
    def get_booking_info(self):
        pass
