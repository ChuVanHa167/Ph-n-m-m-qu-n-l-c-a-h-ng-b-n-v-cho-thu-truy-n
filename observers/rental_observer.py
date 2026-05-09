from observers.observer import Observer

class RentalObserver(Observer):

    def update(self, message):
        print(f"[THÔNG BÁO] {message}")