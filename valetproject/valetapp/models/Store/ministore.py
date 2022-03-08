import copy
from .chainstore import ChainStore


# this acts as a subclass prototype that implements the clone method.
class MiniStore(ChainStore):

    def __str__(self):
        return self.name

    def clone(self):
        return copy.deepcopy(self)
        