from valetapp.interceptor.interceptor import interceptor


class concreteInterceptor1(interceptor):
    def __init__(self) -> None:
        self.contextObject = None

    def callBack(self, contextObject):
        self.contextObject = contextObject
        print(self.get_booking_email_list())

    def get_booking_email_list(self):
        return self.contextObject.get_emails()
