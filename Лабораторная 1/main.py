import doctest


class Groups:
    def __init__(self, order: int, abelian_check: bool = False):
        """
        Создание группы
        :param order: Порядок данной группы
        :param abelian_check: Выбор, будет ли группа абелевой
        """
        if not isinstance(order, int):
            raise TypeError('Порядок группы - натуральное число')
        if not order >= 0:
            raise ValueError('Порядок группы - натуральное число')
        self.order = order

        if not isinstance(abelian_check, bool):
            raise TypeError
        self.abelian_check = abelian_check

    def quotient(self, normal_sub):
        """
        Поиск факторгруппы по заданной нормальной подгруппе
        :param normal_sub: Нормальная подгруппа
        :raise ValueError: Порядок группы должен делиться на порядок подгруппы, иначе - вызываем ошибку
        :return: Полученная факторгруппа

        Пример:
        >>> G = Groups(6)
        >>> H = Groups(2)
        >>> G_H = G.quotient(H)

        """
        if not isinstance(normal_sub, Groups):
            # когда пишу аннотацию типа normal_sub: Groups, выдает ошибку, будто класс Groups ещё не создан
            # а когда пишу проверку принадлежности аргумента к классу Groups через isinstance - никакой ошибки нет
            # почему так?
            raise ValueError('Это не группа')
        ordd = int(self.order/normal_sub.order)
        if not ordd == self.order/normal_sub.order:
            raise ValueError('Подгруппа не из той группы')
        G_H = Groups(ordd)
        return G_H

    def el_check(self, el_ord: int) -> bool:
        """
        Проверка, содержится ли в группе элемент данного порядка
        :param el_ord: Порядок элемента
        :return: Результат проверки

        Пример:
        >>> G = Groups(7)
        >>> G.el_check(5)
        """
        ...


class Fields:
    def __init__(self, order: int, closure_check: bool = False):
        """
        Создание поля
        :param order: Порядок поля
        :param closure_check: Выбор, является ли поле алгебраически замкнутым
        """
        if not isinstance(order, int):
            raise TypeError
        if not order >= 0:
            raise ValueError
        self.order = order

        if not isinstance(closure_check, bool):
            raise TypeError
        self.closure_check = closure_check

    def char(self) -> int:
        """
        Возвращает характеристику данного поля
        :return: Характеристика поля

        Пример:
        >>> F = Fields(9)
        >>> F.char()
        """
        ...

    def closure(self):
        """
        Возвращает замыкание данного поля
        :raise ValueError: Возвращает ошибку, если поле уже замкнуто
        :return: Замыкание, объект класса Fields
        """
        if self.closure_check:
            raise ValueError("Поле уже замкнуто")
        ...

class Rings:
    def __init__(self, num_of_subrings: int, field_check: bool = False):
        """
        Создание кольца
        :param num_of_subrings: Число подколец
        :param field_check: Выбор, является ли кольцо полем
        """
        if not isinstance(field_check, bool):
            raise TypeError
        self.field_check = field_check

        if not isinstance(num_of_subrings, int):
            raise TypeError
        if not num_of_subrings > 0:
            raise ValueError
        self.num_of_subrings = num_of_subrings

    def ext(self, el_num: int):
        # аннотацию типа снова не добавить: ругается, что класс ещё не создан, а я уже пытаюсь писать его в методе
        """
        Построение расширения кольца по данному числу элементов
        :param el_num: Число независимых элементов
        :return: Полученное кольцо, объект класса Rings
        """
        ...

    def fraction_field(self) -> Fields:
        """
        Выдает поле частных данного кольца
        :return: Поле частных, объект класса Fields

        Пример:
        >>> R = Rings(2)
        >>> R.fraction_field()
        """
        ...





if __name__ == "__main__":
    doctest.testmod()

G = Groups(6)
H = Groups(2)
print(G.quotient(H))