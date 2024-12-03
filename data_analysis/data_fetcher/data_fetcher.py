import logging
from meteostat import Daily
import pandas as pd


class WeatherData:
    """
    Класс для получения данных о погоде.
    """

    def __init__(self, location, start_date, end_date):
        """
        Аргументы:
            location (Point): место, для которого получаются данные
            start_date (datetime): начальная дата
            end_date (datetime): конечная дата 

        """
        self.location = location
        self.start_d = start_date
        self.end_d = end_date

        self.__logger = logging.getLogger(__name__)

    def get_weather_data(self) -> pd.DataFrame:
        """
        Получение данных о погоде для заданного местоположения и периода времени.

        Возвращает:
            DataFrame: данные о погоде
        """
        try:
            data = Daily(self.location, start=self.start_d, end=self.end_d)
            weather_data = data.fetch()
            weather_data = weather_data[['tavg']]

            self.__logger.info("Weather data successfully fetched")
            return weather_data

        except Exception as e:
            self.__logger.warning(f"Data get error: {e}")
            return None
