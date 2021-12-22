# class Shape:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self, delta_x, delta_y):
#         self.x = self.x + delta_x
#         self.y = self.y + delta_y
#
#
# class Square(Shape):
#     def __init__(self, side=1, x=0, y=0):
#         super().__init__(x, y)
#         self.side = side

class Rec:
    "self-ссылка на текущий экземпляр класса"
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        self.area_ = self.area(side1, side2)
        self.area_1 = self.count_area(side1, side2)
    "метод класса привязан к классу, а не к экземпляру,принимает класс в качестве параметра"
    @classmethod
    def count_area(cls, _side1, _side2):
        return _side1 * _side2
    "статический метод не знает к какому классу прикреплен" \
    "Статический метод помогает в достижении инкапсуляции в классе, " \
    "поскольку он не знает о состоянии текущего экземпляра. " \
    "Кроме того, статические методы делают код более читабельным и повторно используемым, " \
    "а также более удобным для импорта по сравнению с обычными функциями, " \
    "поскольку каждую функцию не нужно отдельно импортировать."
    @staticmethod
    def area(side_1, side_2):
        return side_1 * side_2

    def notice(self):
        print("Прямоугольник со сторонами" + self.side1 + "и" + self.side2)


R1 = Rec(1, 2)
R2 = Rec(3, 4)
print(R2.area_)
print(R1.area_1)

class Square(Rec):
  def __init__(self, side):
    super().__init__(side1=1, side2=1)



