from valetapp.models.Users.membershiptype import MembershipType
from valetapp.models.Users.staff import Staff
from valetapp.views.Visitor.visitor import Visitor
from valetapp.models.Booking.booking import Booking
from valetapp.models.Store.chainstore import ChainStore
from valetapp.models.Users.customer import Customer
from valetapp.models.Valet.valet import Valet
from valetapp.models.Users.staff import Staff
from valetapp.models.Users.membershiptype import MembershipType


class ConcreteVisitor(Visitor):

    def visit(self, item):
        if isinstance(item, Booking):
            return item.get_price()
        if isinstance(item, Customer):
            return item.getEmail()
        if isinstance(item, ChainStore):
            name = item.get_name()
            return name
        if isinstance(item, Valet):
            name = item.get_name()
            return name
        if isinstance(item, MembershipType):
            return item.get_colour()
        if isinstance(item, Staff):
            return item.get_staff_email()
