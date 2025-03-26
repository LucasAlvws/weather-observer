from app.current_weather_display import CurrentWeatherDisplay
from app.avarage_weather_display import AvarageWeatherDisplay
from app.monitor_tool import MonitorTool

if __name__ == '__main__':
    monitor = MonitorTool()
    current_weather_display = CurrentWeatherDisplay()
    monitor.attach(current_weather_display)

    avarage_weather_display = AvarageWeatherDisplay()
    monitor.attach(avarage_weather_display)
    monitor.update_weather_data()

    avarage_weather_display.start_display()
    current_weather_display.start_display()
