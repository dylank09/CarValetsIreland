import six
from abc import ABCMeta, abstractmethod


@six.add_metaclass(ABCMeta)
class abstract_valet_status(object):

    @abstractmethod
    def get_valet_cost(self):
        pass


class ConcreteValet(abstract_valet_status):

    def get_valet_cost(self):
        return 10


@six.add_metaclass(ABCMeta)
class AbstractValetDecorator(abstract_valet_status):

    def __init__(self, decorated_valet):
        self.decorated_valet = decorated_valet

    def get_valet_cost(self):
        return self.decorated_valet.get_valet_cost()


class WaxCost(AbstractValetDecorator):

    def __init__(self, decorated_valet):
        self.decorated_valet = decorated_valet

    def get_valet_cost(self):
        return self.decorated_valet.get_valet_cost() + 5


class PolishCost(AbstractValetDecorator):

    def __init__(self, decorated_valet):
        self.decorated_valet = decorated_valet

    def get_valet_cost(self):
        return self.decorated_valet.get_valet_cost() + 12


class WashCost(AbstractValetDecorator):

    def __init__(self, decorated_valet):
        self.decorated_valet = decorated_valet

    def get_valet_cost(self):
        return self.decorated_valet.get_valet_cost() + 3


class VacuumCost(AbstractValetDecorator):

    def __init__(self, decorated_valet):
        self.decorated_valet = decorated_valet

    def get_valet_cost(self):
        return self.decorated_valet.get_valet_cost() + 4


class LeatherCost(AbstractValetDecorator):

    def __init__(self, decorated_valet):
        self.decorated_valet = decorated_valet

    def get_valet_cost(self):
        return self.decorated_valet.get_valet_cost() + 6


class SteamCleanCost(AbstractValetDecorator):

    def __init__(self, decorated_valet):
        self.decorated_valet = decorated_valet

    def get_valet_cost(self):
        return self.decorated_valet.get_valet_cost() + 4
