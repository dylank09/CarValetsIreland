from abc import abstractmethod
from django.db import models
from valetapp.models.item import Item

# this acts as both a chainstore and a Prototype interface
class ChainStore(models.Model, Item):
    name = models.CharField(max_length=100)
    longitude = models.DecimalField(max_digits=20, decimal_places=15)
    latitude = models.DecimalField(max_digits=20, decimal_places=15)
    rating = models.IntegerField(default=0)
    maxNumberOfValetsPerHour = models.IntegerField(default=0)

    @abstractmethod
    def clone(self):
        pass

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_max_valets_per_hour(self):
        return self.maxNumberOfValetsPerHour

    def get_longitude(self):
        return self.longitude

    def get_latitude(self):
        return self.latitude

    def accept(self, visitor):
        return visitor.visit(self)

