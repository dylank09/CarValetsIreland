from valetapp.dispatcher.dispatcher import dispatcher
from valetapp.contextObject.contextObject import contextObject


class concreteFramework:
    def __init__(self):
        self.dispatcher = dispatcher()

    def logging(self):
        return 'Hello'

    def event(self):
        print("An event happens here")
        self.contextObject = contextObject(self)
        self.dispatcher.callBack(self.contextObject)
