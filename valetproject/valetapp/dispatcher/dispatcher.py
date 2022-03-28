class dispatcher:
    def __init__(self):
        self.interceptors = []

    def registerInterceptor(self, interceptor):
        self.interceptors.append(interceptor)

    def removeInterceptor(self, interceptor):
        self.interceptors.remove(interceptor)

    def callBack(self, contextObject):
        for interceptor in self.interceptors:
            print("Calling back to: ", interceptor)
            interceptor.callBack(contextObject)
