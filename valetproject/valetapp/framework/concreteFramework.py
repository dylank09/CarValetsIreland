from valetapp.dispatcher.dispatcher import dispatcher
from valetapp.contextObject.contextObject import contextObject
from valetapp.models.Booking.booking import Booking
from valetapp.models.Store.chainstore import ChainStore


class concreteFramework:
    def __init__(self):
        self.dispatcher = dispatcher()

    def access_booking_emails(self):
        bookings = Booking.objects.all()
        email_list = []
        for booking in list(bookings):
            email_list.append(booking.user.getEmail())
        return email_list

    def access_store_names(self): 
        stores = ChainStore.objects.all()
        store_names_list = []
        for store in list(stores):
            store_names_list.append(store.get_name())
        return store_names_list

    def event(self):
        self.contextObject = contextObject(self)
        self.dispatcher.callBack(self.contextObject)
