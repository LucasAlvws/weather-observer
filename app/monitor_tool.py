from random import randint
from app.interfaces.monitor import Monitor
from app.interfaces.oberver import Observer
from contextlib import suppress


class MonitorTool(Monitor):

    def __init__(self):
        super().__init__()
        self.temperature = []
        self.pressure = []
        self.humidity = []
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
        with suppress(IndexError):
            self.temperature.pop()
            self.pressure.pop()
            self.humidity.pop()
        if len(self.temperature) == 9:
            self.temperature.insert(0, randint(0, 35))
            self.pressure.insert(0, randint(10, 100))
            self.humidity.insert(0, randint(900, 1100))
        else:
            self.temperature = [randint(0, 35) for _ in range(10)]
            self.pressure = [randint(10, 100) for _ in range(10)]
            self.humidity = [randint(900, 1100) for _ in range(10)]
        self.notify()
