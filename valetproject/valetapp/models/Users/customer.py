from django.contrib.auth.models import User
from valetapp.models.item import Item
from valetapp.models.Users.observer import Observer
from valetapp.models.Users.membershiptype import MembershipType
from .member import Member


class Customer(Member, Observer, Item):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="valetapp.Customer.user+")
    membershipType = models.ForeignKey(
        MembershipType, on_delete=models.RESTRICT, null=True)

    def __init__(self, *args, factory=None, **kwargs) -> None:
        super().__init__(factory=factory)

    def update(self, subject):
        if subject.get_price() > 0 and self.membershipType != None:

            if self.membershipType.colour == "gold":
                subject.set_price(subject.get_price()*0.7)
            elif self.membershipType.colour == "silver":
                subject.set_price(subject.get_price()*0.8)
            elif self.membershipType.colour == "bronze":
                subject.set_price(subject.get_price()*0.9)

    def get_email(self):
        return self.user.email

    def set_colour(self, membershipType):
        self.membershipType = membershipType

    def accept(self, visitor):
        return visitor.visit(self)
