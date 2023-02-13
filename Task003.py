# Задача 3. Непрерывная случайная величина X распределена нормально и задана плотностью распределения
# f(x) = (1 / (4 * sqrt(2pi))) * exp((-(x+2)**2) / 32)
# Найдите:
# а). M(X)
# б). D(X)
# в). std(X) (среднее квадратичное отклонение)

import numpy


if __name__ == '__main__':

    print('Из формулы f(x) = (1 / (4 * sqrt(2pi))) * exp((-(x+2)**2) / 32)')

    mean = numpy.float64(-2.0)
    print(f'а) M(X) = {mean}')

    dispersion = numpy.float64(16.0)
    print(f'б) D(X) = {dispersion}')

    standard_deviation = numpy.float64(4.0)
    print(f'в) std(X) = {standard_deviation}')