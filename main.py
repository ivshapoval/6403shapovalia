import numpy as np
import sys
import csv


def readconfig():
    rows = []
    with open('config.csv', "r", newline='') as f_read:
        reader = csv.reader(f_read, delimiter=';')
        for row in reader:
            rows.append(row)
    return rows[1]


def fun(begin, step, end, param_a, param_b, param_c):
    data = [['x', 'y']]
    total = 0
    x = 0
    while begin + x <= end:
        y_x = param_a * (1 + (2 * x) / (np.exp(param_b * x) + param_c * param_c)) ** 0.5
        total += y_x
        value = [begin + x, y_x]
        data.append(value)
        x += step
    value = ['total', total]
    data.append(value)
    return data


def writeresult(data):
    with open('results.csv', 'w', newline='') as f_write:
        writer = csv.writer(f_write, delimiter=';')
        for i in range(len(data)):
            writer.writerow(data[i])


if len(sys.argv) > 1:
    print(sys.argv)
    parameters = sys.argv[1:7]
else:
    parameters = readconfig()

n0, h, nk, a, b, c = int(parameters[0]), \
                     int(parameters[1]), \
                     int(parameters[2]), \
                     float(parameters[3]), \
                     float(parameters[4]), \
                     float(parameters[5])

values = fun(n0, h, nk, a, b, c)
writeresult(values)
