class dispatcher:
    def __init__(self):
        self.interceptors = PriorityQueue()

    def registerInterceptor(self, interceptor, priority=1):
        self.interceptors.insert(interceptor, priority)

    def removeInterceptor(self, interceptor):
        self.interceptors.remove(interceptor)

    def callBack(self, contextObject):
        for _ in range(self.interceptors.get_length()):
            current_interceptor = self.interceptors.pop()
            print("Calling back to: ", current_interceptor)
            current_interceptor.callBack(contextObject)


class PriorityQueue():
    def __init__(self) -> None:
        self.queue = {}

    def insert(self, interceptor, priority):
        self.queue[interceptor] = priority

    def remove(self, interceptor):
        del self.queue[interceptor]

    def get_length(self):
        return len(list(self.queue))

    def pop(self):
        top_interceptor = None
        top_value = 0
        for k, v in self.queue.items():
            if v > top_value:
                top_interceptor = k
                top_value = 0
        self.remove(top_interceptor)
        return top_interceptor
