import numpy as np
import sys
import csv


def read_data_from_config_file() -> list:
    """
        Функция парсит config.csv и извлекает параметры оттуда

        Возвращает:
            - list: rows[1] - строка параметров из config.csv
    """
    rows = []
    with open('config.csv', "r", newline='') as f_read:
        reader = csv.reader(f_read, delimiter=';')
        for row in reader:
            rows.append(row)
    return rows[1]


def calculating_the_function_by_steps(begin: float, step: float, end: float, param_a: float, param_b: float,
                                      param_c: float) -> list:
    """
        Функция вычисляет значение функции a * (1 + (2 * x) / (np.exp(param_b * x) + param_c * param_c)) ** 0.5
        по шагам, начиная с begin и заканчивая ближайшим к end значением переменной begin + i * step, где i - счетчик.
        Значения записываются в двумерный массив data, где нулевой элемент каждой строки - аргумент, а первый -
        значение функции при данном аргументе.

        Аргументы:
            - float: begin - начальное значение аргумента
            - float: step - шаг аргумента
            - float: end - конечное значение аргумента
            - float: param_a - параметр а
            - float: param_b - параметр b
            - float: param_c - параметр c

        Возвращает:
            - list: data - матрица значений аргументов и значений функций в этом аргументе
        """
    data = [['x', 'y']]
    total = 0
    x = 0
    while begin + x <= end:
        y_x = param_a * (1 + (2 * x) / (np.exp(param_b * x) + param_c * param_c)) ** 0.5
        total += y_x
        value = [begin + x, y_x]
        data.append(value)
        x += step
    return data


def write_result_to_file(data: list):
    """
            Функция записывает результат функции calculating_the_function_by_steps в файл result.csv

            Аргументы:
                - list: data - матрица значений аргументов и значений функций в этом аргументе
        """
    with open('results.csv', 'w', newline='') as f_write:
        writer = csv.writer(f_write, delimiter=';')
        for i in range(len(data)):
            writer.writerow(data[i])


if len(sys.argv) > 1:
    parameters = sys.argv[1:7]
else:
    parameters = read_data_from_config_file()

n0 = float(parameters[0])
h = float(parameters[1])
nk = float(parameters[2])
a = float(parameters[3])
b = float(parameters[4])
c = float(parameters[5])

values = calculating_the_function_by_steps(n0, h, nk, a, b, c)
write_result_to_file(values)
