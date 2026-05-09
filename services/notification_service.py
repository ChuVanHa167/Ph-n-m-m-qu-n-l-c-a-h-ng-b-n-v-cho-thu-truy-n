from observers.observer import Observer


class NotificationService:

    _instance = None

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.observers = []

        return cls._instance

    def add_observer(self, observer: Observer):

        if observer not in self.observers:
            self.observers.append(observer)

    def notify(self, message):

        for observer in self.observers:
            observer.update(message)