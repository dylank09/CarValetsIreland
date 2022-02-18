from django.db import models
from valetapp.models.item import Item


class Valet(models.Model, Item):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def accept(self, visitor):
        return visitor.visit(self)
