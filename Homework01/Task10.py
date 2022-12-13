# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math


def get_point_coorditate():
    point_coordinate = list(map(int, input('Введите координаты точки через запятую(сначала абциссу, затем ординату): ').split(',')))
    return point_coordinate

first_point = get_point_coorditate()
second_point = get_point_coorditate()
distance = math.sqrt(((second_point[0] - first_point[0])**2) +(second_point[1] - first_point[1])**2)
print(f'Расстояние между точкой А({first_point[0]}, {first_point[1]}) и B({second_point[0]}, {second_point[1]}) равно {round(distance, 2)}')