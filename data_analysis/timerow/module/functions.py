import pandas as pd
import numpy as np
from math import nan
from typing import Any, Callable
from timerow.module.integer_generator import integer_generator
# здесь был изменен путь к генератору

def log_function_decorator(func : Callable) -> Callable:
    '''
        Декоратор для логирования функций
    '''
    def wrapper(*args : Any, **kwargs : Any):
        with open('log.txt', 'a', encoding='utf-8') as f:
              f.write(f"Вызов функции: {func.__name__} с аргументами: {args} {kwargs}")
              result = func(*args, **kwargs)
              f.write(f"Результат: {result}")
        return result
    return wrapper 


class WeatherData:
    """
    Класс для работы с погодными данными

    Атрибуты:
        - pd.Series: data - данные о погоде
    """

    @log_function_decorator
    def __init__(self, data) -> None:
        """
        Инициализирует объект WeatherData

        Аргументы:
            - pd.Series: data - массив данных о погоде
        """

        self.data = data


    @log_function_decorator
    def get_data(self):
        """
        Возвращает данные о погоде

        Возвращает:
            - pd.DataFrame: data - массив данных о погоде
        """

        return self.data


    @log_function_decorator
    def moving_average(self, window: int) -> None:
        """
        Вычисляет скользящее среднее значение температуры в неком окне

        Аргументы:
            - int: window - размер окна в днях
        """

        ma_column = f'moving_average_{window}'
        self.data[ma_column] = self.data['tavg'].rolling(window=window).mean()


    @log_function_decorator
    def calculate_difference(self, window: int) -> None:
        """
        Вычисляет разницу между последовательными значениями скользящего среднего

        Аргументы:
            - int: window - размер окна для скользящего среднего значения в днях
        """
        ma_column = f'moving_average_{window}'
        if ma_column not in self.data:
            self.moving_average(window)
        self.data['temperature_difference'] = self.data[ma_column].diff()


    @log_function_decorator
    def autocorrelation(self, window: int) -> None:
        """
        Вычисляет автокорреляцию скользящего среднего

        Аргументы:
            int: window - размер окна для скользящего среднего в днях
        """

        autoc = f'autocorrelation{window}'
        data_len = len(self.data)
        max_lag = data_len - 1 # максимальный лаг
        autocorr = []
        for lag in range(1, max_lag+2):
            if lag >= window:
                autocorr.append(float(self.data['tavg'].autocorr(lag)))
            else:
                autocorr.append(nan)
        self.data['autoc'] = autocorr
        return pd.Series(autocorr, index=np.arange(1, max_lag+2))


    @log_function_decorator
    def find_extremal(self, window: int) -> pd.DataFrame:
        """
        Находит экстремальные значения скользящего среднего

        Аргументы:
            int: window - размер окна для скользящего среднего в днях

        Возвращает:
            pd.DataFrame: extremal - экстремальные значения скользящего среднего
        """
        ma_column = f'moving_average_{window}'
        if ma_column not in self.data:
            self.moving_average(window)
        extremal = self.data[ma_column][self.data[ma_column].diff().ne(0)]
        self.data['extremal'] = extremal
        return extremal        
