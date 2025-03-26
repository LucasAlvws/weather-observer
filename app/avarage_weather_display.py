import tkinter as tk

from app.interfaces.oberver import Observer
from app.monitor_tool import MonitorTool


class AvarageWeatherDisplay(Observer):
    def __init__(self):
        super().__init__()
        self._display = tk.Tk()
        self._display.title("Clima Médio, temperatura, pressão e humidade")
        self._weather_label = tk.Label(self._display, text='')
        self._weather_label.pack()

    def update(self, data, monitor: MonitorTool) -> None:
        """
        Receive update from monitor tool.
        """
        temperature = 0
        pressure = 0
        humidity = 0
        for i in range(10):
            temperature += data.get('temperature')[i]
            pressure += data.get('pressure')[i]
            humidity += data.get('humidity')[i]
        
        text = f"Temperatura: {temperature/10} Pressão: {pressure/10} Humidade: {humidity/10}\n"
        self._weather_label.config(text=text)
        self._display.after(13400, monitor.update_weather_data)

    def start_display(self):
        self._display.mainloop()
