import pandas as pd
import logging


def window_generator(data: pd.Series, window: int):
    """
    Генерирует скользящие окна для данных

    Аргументы:
        data (pd.Series): временной ряд для анализа
        window (int): размер окна для скользящего среднего

    Возвращает:
        generator: генератор, который выдает скользящие окна данных
    """
    for i in range(len(data) - window + 1):
        yield data[i:i + window]


class WeatherData:
    """
    Класс для анализа временных рядов

    Поля:
        data (pd.Series): временной ряд для анализа
    """

    def __init__(self, data: pd.Series):
        """
        Инициализирует объект с временным рядом

        Аргументы:
            data (pd.Series): временной ряд для анализа
        """
        self.data = data
        self.__logger = logging.getLogger(__name__)


    def moving_average(self, window: int) -> pd.Series:
        """
        Вычисляет скользящее среднее

        Аргументы:
            window (int): размер окна для скользящего среднего

        Возвращает:
            pd.Series: временной ряд со значениями скользящего среднего
        """
        self.__logger.info("Вычисление скользящего среднего")
        return self.data.rolling(window=window).mean()


    def differentiate(self, data: pd.Series) -> pd.Series:
        """
        Вычисляет дифференциал временного ряда.

        Возвращает:
            pd.Series: временной ряд с вычисленными разностями
        """
        self.__logger.info("Вычисление дифференциала")
        return data.diff()


    def autocorrelation(self, lag: int) -> float:
        """
        Вычисляет автокорреляцию временного ряда с заданным лагом

        Аргументы:
            lag (int): лаг для автокорреляции

        Возвращает:
            float: значение автокорреляции для заданного лага
        """
        return self.data.autocorr(lag)


    def global_max_min(self):
        """
        Вычисляет глобальный максимум и минимум временного ряда

        Возвращает:
            tuple: Глобальный максимум и минимум.
        """
        self.__logger.info("Вычисление максимума и минимума")
        global_max = self.data.max()
        global_min = self.data.min()
        return global_max, global_min


    def analyze_the_trend(self, window: int) -> pd.DataFrame:
        """
        Анализирует сезонность и тренд временного ряда.

        Аргументы:
            window (int): Размер окна для скользящего среднего.

        Возвращает:
            pd.DataFrame: Результат анализа (оригинальные данные, скользящее среднее,
                          дифференциал и автокорреляция).
        """
        self.__logger.info("Анализ временного ряда")
        average = self.moving_average(window)
        differential = self.differentiate(average)
        self.__logger.info("Вычисление автокорреляции")
        autocorr_values = [self.autocorrelation(lag) for lag in range(len(self.data))]

        # Получаем глобальный максимум и минимум
        global_max, global_min = self.global_max_min()
        print(f"Глобальный максимум: {global_max}, Глобальный минимум: {global_min}")

        result = pd.DataFrame({
            'orig': self.data,
            'moving_average_{window}': average,
            'diff': differential,
            'autocorr': autocorr_values
        })

        return result