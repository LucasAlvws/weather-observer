from random import randint
from app.interfaces.monitor import Monitor
from app.interfaces.oberver import Observer


class MonitorTool(Monitor):

    def __init__(self):
        super().__init__()
        self.temperature = 0
        self.pressure = 0
        self.humidity = 0
        self._observers = []

    def attach(self, observer: Observer):
        """
        Attach an observer to the subject.
        """
        self._observers.append(observer)

    def detach(self, observer: Observer):
        """
        Detach an observer from the subject.
        """
        self._observers.remove(observer)

    def notify(self):
        """
        Notify all observers about an event.
        """
        for observer in self._observers:
            data = {
                'temperature': self.temperature,
                'pressure': self.pressure,
                'humidity': self.humidity,
            }
            observer.update(data, self)

    def update_weather_data(self):
        self.temperature = randint(0, 200)
        self.pressure = randint(0, 200)
        self.humidity = randint(0, 200)
        self.notify()
