from valetapp.interceptor.interceptor import interceptor


class concreteInterceptor2(interceptor):
    def __init__(self,) -> None:
        self.contextObject = None

    def callBack(self, contextObject):
        self.contextObject = contextObject
        print(self.get_store_names_list())

    def get_store_names_list(self):
        return self.contextObject.get_store_names()
