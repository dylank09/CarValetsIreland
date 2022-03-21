from valetapp.dispatcher.dispatcher import dispatcher
from valetapp.contextObject.contextObject import contextObject
from valetapp.models.Booking.booking import Booking


class concreteFramework:
    def __init__(self):
        self.dispatcher = dispatcher()

    def access_booking_emails(self):
        bookings = Booking.objects.all()
        email_list = []
        for booking in list(bookings):
            email_list.append(booking.user.getEmail())
        return email_list

    def event(self):
        self.contextObject = contextObject(self)
        self.dispatcher.callBack(self.contextObject)
