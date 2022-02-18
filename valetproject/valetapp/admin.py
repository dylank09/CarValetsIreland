from django.contrib import admin
from valetapp.models.Store.chainstore import ChainStore
from valetapp.models.Users.customer import Customer
from valetapp.models.Users.staff import Staff
from valetapp.models.Booking.booking import Booking
from valetapp.models.Valet.valet import Valet
from valetapp.models.Users.membershiptype import MembershipType
admin.site.register(Customer)
admin.site.register(Staff)
admin.site.register(ChainStore)
admin.site.register(Booking)
admin.site.register(Valet)
admin.site.register(MembershipType)
