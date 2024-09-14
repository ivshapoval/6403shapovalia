import numpy as np
import sys

def readconfig():
    results = []
    with open('config.csv', 'r') as fread:
        text = fread.read()
        for line in text.split('\n'):
            items = line.split(';')
            results.append(items)
    return results[1]


def fun(n0, h, nk, a, b, c):
    value = 0
    for x in range(n0, nk, h):
        value += a * (1 + (2 * x) / (np.exp(b * x) + c * c)) ** 0.5
    return value


def writeresult(value):
    with open('results.csv', 'w') as fwrite:
        fwrite.write(str(value))
    return


parameters = []
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

y = fun(n0, h, nk, a, b, c)

writeresult(y)
