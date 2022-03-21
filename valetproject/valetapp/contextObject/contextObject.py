

class contextObject:
    def __init__(self, concreteFramework) -> None:
        self.concreteFramework = concreteFramework

    def get_emails(self):
        return self.concreteFramework.access_booking_emails()

    def get_store_names(self):
        return self.concreteFramework.access_store_names()
