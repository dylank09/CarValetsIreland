from valetapp.interceptor.interceptor import interceptor


class concreteInterceptor(interceptor):
    def __init__(self,) -> None:
        self.contextObject = None

    def callBack(self, contextObject):
        self.contextObject = contextObject

    def log(self):
        return self.contextObject.log()
