from typing import Any, List


class Observable:
    def __init__(self) -> None:
        self._observers: List[Any] = []
        self._changed = False

    def add_observer(self, observer: Any) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer: Any) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, *args, **kwargs) -> None:
        if self._changed:
            for observer in self._observers:
                observer.update(self, *args, **kwargs)
            self._changed = False

    def set_state(self) -> None:
        self._changed = True

    def clear_state(self) -> None:
        self._changed = False

    def get_state(self) -> bool:
        return self._changed


class Observer:
    def update(self, observable: Any, *args, **kwargs) -> None:
        pass


class WeatherData(Observable):
    _temperature = 0.0
    _humidity = 0.0
    _pressure = 0.0

    @property
    def temperature(self) -> float:
        return self._temperature

    @temperature.setter
    def temperature(self, val: float) -> None:
        self._temperature = val
        self.set_state()
        self.notify()

    @property
    def humidity(self) -> float:
        return self._humidity

    @humidity.setter
    def humidity(self, val: float) -> None:
        humidity_diff = abs(self._humidity - val) if self._humidity else 0

        self._humidity = val

        if humidity_diff > 0.1:
            self.set_state()
            self.notify()

    @property
    def pressure(self) -> float:
        return self._pressure

    @pressure.setter
    def pressure(self, val: float) -> None:
        self._pressure = val
        self.set_state()
        self.notify()


class WeatherTemperatureDisplay(Observer):
    def update(self, observable: Any, *args, **kwargs) -> None:
        self._temperature = observable.temperature
        self.display()

    def display(self) -> None:
        print(f"Curent temperature is {self._temperature}")


class WeatherHumidityDisplay(Observer):
    def update(self, observable: Any, *args, **kwargs) -> None:
        self._humidity = observable.humidity
        self.display()

    def display(self) -> None:
        print(f"Curent humidity is {self._humidity}")


class WeatherPressureDisplay(Observer):
    def update(self, observable: Any, *args, **kwargs) -> None:
        self._pressure = observable.pressure
        self.display()

    def display(self) -> None:
        print(f"Curent pressure is {self._pressure}")


def main():
    weather_data = WeatherData()
    weather_data.temperature = 1.0
    weather_data.pressure = 1.0
    weather_data.humidity = 1.0

    weather_temperature_display = WeatherTemperatureDisplay()
    weather_data.add_observer(weather_temperature_display)

    weather_humidity_display = WeatherHumidityDisplay()
    weather_data.add_observer(weather_humidity_display)

    weather_pressure_display = WeatherPressureDisplay()
    weather_data.add_observer(weather_pressure_display)

    weather_data.temperature = 51.0
    weather_data.pressure = 13.37
    weather_data.pressure = 13.37
    weather_data.humidity = 3.0
    weather_data.humidity = 3.01
    weather_data.humidity = 3.5


if __name__ == "__main__":
    main()
