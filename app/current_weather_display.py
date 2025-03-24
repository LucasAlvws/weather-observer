import tkinter as tk

from app.interfaces.oberver import Observer
from app.monitor_tool import MonitorTool


class CurrentWeatherDisplay(Observer):
    def __init__(self):
        super().__init__()
        self._display = tk.Tk()
        self._temperature_label = tk.Label(text='')
        self._temperature_label.pack()
        self._pressure_label = tk.Label(text='')
        self._pressure_label.pack()
        self._humidity_label = tk.Label(text='')
        self._humidity_label.pack()

    def update(self, data, monitor: MonitorTool) -> None:
        """
        Receive update from monitor tool.
        """

        self._temperature_label.config(text=f"{data.get('temperature', None)}")
        self._pressure_label.config(text=f"{data.get('pressure', None)}")
        self._humidity_label.config(text=f"{data.get('humidity', None)}")
        self._display.after(5000, monitor.update_weather_data)

    def start_display(self):
        self._display.mainloop()
