# Задача 5. На сколько сигм (средних квадратичных отклонений) отклоняется рост человека,
# равный 190 см, от математического ожидания роста в популяции, в которой
# M(X) = 178 см и D(X) = 25 кв.см?


import math

std=math.sqrt(25)
sigma=(190-178)/std
print(f'Рост человека, равный 190 см, отклоняется от математического ожидания роста в популяции, \n'
      f'на {sigma} сигм.')