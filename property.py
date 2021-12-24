class Rec:
    list_of_rectangles = [] #создаю пустой список для работы с методом класса
    "self-ссылка на текущий экземпляр класса"
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        self.area_ = self.area(side1, side2)
        Rec.list_of_rectangles.append(self) # добавляю в список экземпляр класса прямоугольник
    "метод класса привязан к классу, а не к экземпляру,принимает класс в качестве параметра"
#    @classmethod
#    def count_area(cls, _side1, _side2):
#       return _side1 * _side2 ТУТ У МЕНЯ БЫЛО НЕ ТО ЧТО НУЖНО
    @classmethod
    def count_all_areas(cls):
        s = 0 #изначально сумма площадей экземляров равна нулю
        for i in Rec.list_of_rectangles: # циклом проходимся по списку экземпляров класса и считаем их сумму
            s += i.side1 * i.side2
        return s #возвращаем посчитанную сумму

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

class Square(Rec):
  def __init__(self, side):
    super().__init__(side, side)


R1 = Rec(1, 2)
R2 = Rec(3, 4)
S1 = Square(2)
S2 = Square(5)
print(R1.area_)
print(S1.area(S1.side1, S1.side2)) #метод area доступен классу square наследнику класса rec
print(Rec.count_all_areas())



