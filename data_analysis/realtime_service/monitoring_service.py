import threading
import logging
import numpy as np
from data_fetcher import data_fetcher
from timerow.module.functions import WeatherData


class DataMonitor(threading.Thread):
    def __init__(self, location: np.ndarray, start_date: str, end_date: str, interval):
        """
        Инициализация класса DataMonitor

        Аргументы:
            location (Point): место, для которого получаются данные
            start_date (datetime): начальная дата
            end_date (datetime): конечная дата 
            interval (int): интервал в секундах, с которым будет выполняться проверка новых данных
        """
        super().__init__()
        self.location = location
        self.interval = interval
        self.start_d = start_date
        self.end_d = end_date
        self.__logger = logging.getLogger(__name__)
        self._stop_event = threading.Event()

    def run(self):
        """
        Запускает цикл мониторинга данных
        """
        self.__logger.info("Monitoring started")
        while not self._stop_event.is_set():
            try:
                # Получаем текущие данные о погоде
                current_data = data_fetcher.WeatherData(self.location, self.start_d, self.end_d)
                current_data = current_data.get_weather_data()
                if current_data is not None and not current_data.empty:
                    print(f"Current data of weather: {current_data}")
                # Пример временного ряда (температура)
                temperature_series = current_data['tavg']
                # Создаем экземпляр класса для анализа временного ряда
                analyzer = WeatherData.data
                # Анализируем тренд и сезонность
                result = analyzer.analyze_the_trend(window=7)
                print(result)
            except Exception as e:
                self.__logger.warning(f"Thread error in monitoring: {e}")
                break
            self._stop_event.wait(self.interval)

    def stop(self):
        """
        Останавливает цикл мониторинга
        """
        self._stop_event.set()
        self.join()
        self.__logger.info("Monitoring stopped")
