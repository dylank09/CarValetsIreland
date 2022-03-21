from valetapp.interceptor.interceptor import interceptor


class concreteInterceptor(interceptor):
    def __init__(self,) -> None:
        self.contextObject = None

    def callBack(self, contextObject):
        self.contextObject = contextObject

    def get_booking_email_list(self):
        return self.contextObject.get_emails()
