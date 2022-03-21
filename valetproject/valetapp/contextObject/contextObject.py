

class contextObject:
    def __init__(self, concreteFramework) -> None:
        self.concreteFramework = concreteFramework

    def get_emails(self):
        return self.concreteFramework.access_booking_emails()
