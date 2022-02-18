from django.db import models
from django.contrib.auth.models import User
from valetapp.models.item import Item
from valetapp.models.Users.observer import Observer
from valetapp.models.Users.membershiptype import MembershipType


class Customer(models.Model, Observer, Item):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    membershipType = models.ForeignKey(
        MembershipType, on_delete=models.RESTRICT, null=True)

    def update(self, subject):
        if subject.get_price() > 0 and self.membershipType != None:

            if self.membershipType.colour == "gold":
                subject.set_price(subject.get_price()*0.7)
            elif self.membershipType.colour == "silver":
                subject.set_price(subject.get_price()*0.8)
            elif self.membershipType.colour == "bronze":
                subject.set_price(subject.get_price()*0.9)

    def getEmail(self):
        return self.user.email

    def set_colour(self, membershipType):
        self.membershipType = membershipType

    def accept(self, visitor):
        return visitor.visit(self)
