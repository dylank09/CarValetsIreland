from abc import ABC, abstractmethod


class narrowInterface(ABC):

    @abstractmethod
    def get_customer_emails(self):
        pass

    @abstractmethod
    def get_total_money(self):
        pass

    @abstractmethod
    def get_money_by_each_store(self):
        pass

    @abstractmethod
    def get_stores(self):
        pass

    @abstractmethod
    def get_valets(self):
        pass

    @abstractmethod
    def get_membership_types(self):
        pass

    @abstractmethod
    def get_staff(self):
        pass