
if __name__ == "__main__":
    class Molecules:
        def __init__(self, name: str, atom_num: int, atom_mass: list[int]):
            """
            Создание и подготовка к работе класса "Молекулы"

            :param name: Название молекулы
            :param atom_num: Число атомов
            :param atom_mass: Массы всех атомов (в количестве нуклонов) в произвольном порядке в виде списка

            Пример
            >>> h2o = Molecules('вода', 3, [1,1,8])  # создание экземпляра класса

            """
            self.name = name
            if atom_num > 0:
                self.atom_num = atom_num
            else:
                raise AttributeError("Количество атомов - положительное число")
            if len(atom_mass) == atom_num:
                self.atom_mass = atom_mass
            else:
                raise ValueError("Атомные массы не соответствуют числу атомов")

        def __str__(self):
            return f"Молекула {self.name} содержит атомов: {self.atom_num}"

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, atom_num = {self.atom_num!r})"

        def reaction(self, mol2):
            """
            Реакция молекулы self с молекулой mol2
            :param mol2: Вторая молекула реагент
            :raise ValueError: Вторая молекула должна принадлежать классу Molecules, иначе - вызов ошибки
            :return: Полученная молекула - экземпляр класса Molecules

            Пример
            >>> h2 = Molecules('водород', 2, [1,1])
            >>> o2 = Molecules('кислород',2, [8,8])
            >>> mol3 = h2.reaction(o2)
            """
            if not isinstance(mol2, Molecules):
                raise ValueError("Второй реагент должен быть молекулой!")
            ...

        def mol_type(self) -> str:
            """
            Тип молекулы
            :return: Строка с описанием типа молекулы (простая/сложная)

            Пример
            >>> h2 = Molecules('водород', 2, [1,1])
            >>> h2o = Molecules('вода', 3, [1,1,8])
            >>> h2.mol_type()
            'Простое вещество'
            >>> h2o.mol_type()
            'Сложное вещество'
            """
            if len(set(self.atom_mass)) == 1:
                return "Простое вещество"
            else:
                return "Сложное вещество"


    class CarbHyd(Molecules):
        def __init__(self, name: str, atom_num: int, atom_mass: list[int], mon_num: int):
            """
            Создание и подготовка к работе класса "Углеводы"
            :param name: Название молекулы
            :param atom_num: Число атомов
            :param atom_mass: Массы всех атомов (в количестве нуклонов) в произвольном порядке в виде списка
            :param mon_num: Число мономеров

            Пример
            >>> glu = CarbHyd('глюкоза', 24, [1,1,8,12]*6, 1)  # создание экземпляра класса

            """
            super().__init__(name, atom_num, atom_mass)
            if mon_num > 0:
                self.mon_num = mon_num
            else:
                raise ValueError("Количество мономеров - положительное число")

        def __str__(self):
            return f"Углевод {self.name} содержит мономеров: {self.mon_num}"

        def mol_type(self) -> str:
            """
            Тип углеводной молекулы.
            Все углеводы - сложные вещества, поэтому метод материнского класса не имеет смысла, детализуем описание
            :return: Строка с типом молекулы в зависимости от числа мономеров

            Пример
            >>> glu = CarbHyd('глюкоза', 24, [1,1,8,12]*6, 1)
            >>> glu.mol_type()
            'Моносахарид'
            >>> malt = CarbHyd('мальтоза', 45, [12]+[1,1,8,12]*11, 2)
            >>> malt.mol_type()
            'Олигосахарид'

            """
            if self.mon_num == 1:
                return "Моносахарид"
            elif self.mon_num <= 10:
                return "Олигосахарид"
            else:
                return "Полисахарид"


    pass
