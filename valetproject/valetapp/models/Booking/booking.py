from django.db import models
from enum import Enum
from valetapp.models.Users.customer import Customer
from valetapp.models.subject import Subject
from valetapp.models.Store.chainstore import ChainStore
from valetapp.models.item import Item


class BookingStates(Enum):
    PENDING = 'pending'  # when a booking is made but not paid for
    BOOKED = 'booked'  # when booking is paid for
    CANCELLED = 'cancelled'  # when booking is cancelled

    @classmethod
    def tuples(cls): return tuple((state.name, state.value) for state in cls)


class Booking(models.Model, Subject, Item):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    store = models.ForeignKey(ChainStore, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    booking_state = models.CharField(
        max_length=20, choices=BookingStates.tuples(), default=BookingStates.PENDING)
    valetservice = models.CharField(max_length=200, default="")
    price = models.FloatField(default=0.00)

    observers = []

    def pending(self):
        self.booking_state = 'PENDING'

    def book(self):
        self.booking_state = 'BOOKED'

    def cancel(self):
        self.booking_state = 'CANCELLED'

    def endtime(self): self.booking_state = BookingStates.END_TIME

    def get_booking_status(self): return self.booking_state

    def get_price(self): return self.price

    def get_store(self): return self.store

    def get_start_time(self): return self.start_time

    def set_price(self, new_price): self.price = new_price

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def __str__(self):
        return f'{self.user} has booked {self.start_time} until {self.end_time}'

    def accept(self, visitor):
        return visitor.visit(self)
