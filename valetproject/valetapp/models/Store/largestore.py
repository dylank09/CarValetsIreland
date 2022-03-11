import copy
from .chainstore import ChainStore
from django.db import models


class LargeStore(ChainStore):
    numAutoValets = models.IntegerField(default=1) # a store qualifies as large if it has at least 1 auto valet machine

    def __str__(self):
        return self.name

    def clone(self):
        return copy.deepcopy(self)