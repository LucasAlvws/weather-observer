from app.current_weather_display import CurrentWeatherDisplay
from app.monitor_tool import MonitorTool
if __name__ == '__main__':
    display = CurrentWeatherDisplay()
    monitor = MonitorTool()
    monitor.attach(display)
    monitor.update_weather_data()
    display.start_display()