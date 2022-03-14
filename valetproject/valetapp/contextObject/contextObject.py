

class contextObject:
    def __init__(self, concreteFramework) -> None:
        self.concreteFramework = concreteFramework

    def log(self):
        return self.concreteFramework.logging()
