import tkinter as tk

from app.interfaces.oberver import Observer
from app.monitor_tool import MonitorTool


class CurrentWeatherDisplay(Observer):
    def __init__(self):
        super().__init__()
        self._display = tk.Tk()
        self._display.title("Clima atual, temperatura, pressão e humidade")
        self._weather_label = tk.Label(self._display, text='')
        self._weather_label.pack()

    def update(self, data, monitor: MonitorTool) -> None:
        """
        Receive update from monitor tool.
        """
        text = ''
        for i in range(10):
            text += f"Temperatura: {data.get('temperature')[i]} Pressão: {data.get('pressure')[i]} Humidade: {data.get('humidity')[i]}\n"
        self._weather_label.config(text=text)
        self._display.after(16000, monitor.update_weather_data)

    def start_display(self):
        self._display.mainloop()
