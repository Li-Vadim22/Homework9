'''
2.Реализовать класс Road(дорога). oпределить атрибуты: length(длина), width(ширина); значени атрибутов должны
передаваться при создании экземпляра класса; атрибуты сделать защищёнными; определить метод расчёта массы
асфальта, необходимого для покрытия всей дороги; использовать формулу: длина * ширина * массаасфальта для покрытия
одного кв.метра дороги асфальтом, толщиной в 1 см * число см толщины полотна; проверить работу метода.

Например: 20 м * 5000 м * 25кг * 5см = 12500 т.
'''
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self):
        mass = self._length * self._width * 25 * 5 / 1000
        return mass


my_road = Road(20, 5000)
print(my_road.calc_mass(),'т')

