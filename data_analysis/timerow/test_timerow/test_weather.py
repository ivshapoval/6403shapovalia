import unittest
import pandas as pd
import numpy as np
from module.functions import WeatherData

# тесты вызывают функцию и проверяют, вызвалась ли она
# assertIn проверяет, входит ли первый аргумент во второй (weather_data.data.columns) 

class TestWeatherData(unittest.TestCase):

    def setUp(self):
        '''
        Создание тестового набора данных. Этот метод вызвается при каждом тесте
        '''

        data = {
            # тестовые значения для инициализации WeatherData
            'tavg': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        }

        self.df = pd.DataFrame(data)
        self.weather_data = WeatherData(self.df)

    def test_get_data(self):
        '''
        Проверяет, что возвращаемый результат равен исходному
        '''

        result = self.weather_data.get_data()
        self.assertTrue(result.equals(self.df))

    def test_moving_average(self):
        '''
        Проверяет, что в self.weather_data.data.columns появился столбец 'moving_average_311'
        '''

        self.weather_data.moving_average(311)
        self.assertIn('moving_average_311', self.weather_data.data.columns)

    def test_calculate_difference(self):
        '''
        Проверяет, что в self.weather_data.data.columns появился столбец 'temperature_difference'
        '''

        self.weather_data.calculate_difference(311)
        self.assertIn('temperature_difference', self.weather_data.data.columns)

    def test_autocorrelation(self):
        '''
        Сравнивает теоретическое значение и значение из реализованной функции
        '''
        
        result = self.weather_data.autocorrelation()
        expected_result = self.weather_data.data['tavg'].autocorr(1)

        self.assertTrue(result[1], expected_result)

    def test_find_extremal(self):
        '''
        Проверяет, что в self.weather_data.data.columns появился столбец 'extremal'
        '''
        
        self.weather_data.find_extremal(311)
        self.assertIn('extremal', self.weather_data.data.columns)
