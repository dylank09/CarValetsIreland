from valetapp.models.Booking.booking import Booking
from valetapp.models.Users.customer import Customer
from valetapp.models.Store.chainstore import ChainStore
from valetapp.models.Valet.valet import Valet
from valetapp.models.Users.membershiptype import MembershipType
from valetapp.models.Users.staff import Staff
from abc import ABC, abstractmethod
from valetapp.views.Visitor.concreteVisitor import ConcreteVisitor
from django.shortcuts import render

from valetapp.views.Visitor.narrowInterface import narrowInterface


class exportToCSV_Adapter(narrowInterface):

    def __init__(self):
        self.bookings = Booking.objects.all()
        self.customers = Customer.objects.all()
        self.stores = ChainStore.objects.all()
        self.valets = Valet.objects.all()
        self.membershipTypes = MembershipType.objects.all()
        self.staffs = Staff.objects.all()
        self.visitor = ConcreteVisitor()

    def get_customer_emails(self):
        customer_emails = []
        for customer in self.customers:
            customer_emails.append(customer.accept(self.visitor))
        return customer_emails

    def get_total_money(self):
        total_sum = 0
        for booking in self.bookings:
            total_sum += booking.accept(self.visitor)
        print(total_sum)
        return total_sum

    def get_money_by_each_store(self):
        money_made_by_store = []
        for store in self.stores:
            store_total = 0
            for booking in self.bookings:
                if(booking.get_store() == store):
                    store_total += booking.get_price()
            money_made_by_store.append((store.get_name(), store_total))
        return money_made_by_store

    def get_stores(self):
        store_names = []
        for store in self.stores:
            store_names.append(store.accept(self.visitor))
        return store_names

    def get_valets(self):
        valet_types = []
        for valet in self.valets:
            valet_types.append(valet.accept(self.visitor))
        return valet_types

    def get_membership_types(self):
        membership_types = []
        for membershipType in self.membershipTypes:
            membership_types.append(membershipType.accept(self.visitor))
        return membership_types

    def get_staff(self):
        staff_members = []
        for staff in self.staffs:
            staff_members.append(staff.accept(self.visitor))
        return staff_members
