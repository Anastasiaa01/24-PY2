# TODO Написать 3 класса с документацией и аннотацией типов
class Triangle:
    def __init__(self, first_side: (int, float), second_side: (int, float), third_side: (int, float)):
        """
        Создание и подготовка к работе объекта "Треугольник"

        :param first_side: первая сторона треугольника
        :param second_side: вторая сторона треугольника
        :param third_side: третья сторона треугольника

        Примеры:
        >>> triangle = Triangle(10, 5, 15)  # инициализация экземпляра класса
        """
        if not isinstance(first_side, (int, float)):
            raise TypeError("Необходимо ввести число типа int или float")
        if first_side <= 0:
            raise ValueError("Число должно быть положительным")
        self.first_side = first_side
        if not isinstance(second_side, (int, float)):
            raise TypeError("Необходимо ввести число типа int или float")
        if second_side <= 0:
            raise ValueError("Число должно быть положительным")
        self.second_side = second_side
        if not isinstance(third_side, (int, float)):
            raise TypeError("Необходимо ввести число типа int или float")
        if third_side <= 0:
            raise ValueError("Число должно быть положительным")
        self.third_side = third_side

    def is_equilateral(self) -> bool:
        """
        Функция которая проверяет является ли треугольник равносторонним

        :return: Является ли треугольник равносторонним

        Примеры:
        >>> triangle = Triangle(10, 5, 15)
        >>> triangle.is_equilateral()
        """
    def is_exists(self) -> bool:
        """
        Функция которая проверяет существует ли треугольник с текущими сторонами

        :return: Cуществует ли треугольник с текущими сторонами

        Примеры:
        >>> triangle = Triangle(10, 1, 15)
        >>> triangle.is_exists()
        """

class Person:
    def __init__(self, name: str, age: int):
        """
        Создание и подготовка к работе объекта "Человек"

        :param name: имя человека
        :param age: Возраст человека

        Примеры:
        >>> person = Person('Misha', 30)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой типа str")
        self.name = name
        if not isinstance(age, int):
            raise TypeError("Возраст должен быть числом типа int")
        if age <= 0:
            raise ValueError("Возраст должен быть положительным числом")
        self.age = age

    def is_adult(self) -> bool:
        """
        Функция которая проверяет является ли человек совершеннолетним

        :return: Является ли человек совершеннолетним

        Примеры:
        >>> person = Person('Misha', 30)
        >>> person.is_adult()
        """
    def information(self) -> str:
        """
        Функция которая формирует строку с информацией о человеке (имя и возраст)

        :return: Имя и возраст человека

        Примеры:
        >>> person = Person('Misha', 30)
        >>> person.information()
        """

class Budget:
    def __init__(self, money: (int, float)):
        """
        Создание и подготовка к работе объекта "Бюджет"

        :param money: имеющийся бюджет

        Примеры:
        >>> budget = Budget(100000)  # инициализация экземпляра класса
        """

        if not isinstance(money, (int, float)):
            raise TypeError("Необходимо ввести число типа int или float")
        if money < 0:
            raise ValueError("Число должно быть положительным")
        self.money = money

    def plus(self, value: (int, float)) -> None:
        """
        Увеличение бюджета на определенную сумму.

        :param value: Сумма на которую увеличивается бюджет


        Примеры:
        >>> budget = Budget(100000)
        >>> budget.plus(50000)
        """

        if not isinstance(value, (int, float)):
            raise TypeError("Введенная сумма должна быть типа int или float")
        if value < 0:
            raise ValueError("Введенная сумма должна положительным числом")

    def minus(self, value: (int, float)) -> None:
        """
        Уменьшение бюджета на определенную сумму.

        :param value: Сумма на которую уменьшается бюджет

        :raise ValueError: Если ввели сумму превышающую имеющийся бюджет, то вызывается ошибка

        Примеры:
        >>> budget = Budget(100000)
        >>> budget.minus(30000)
        """

        if not isinstance(value, (int, float)):
            raise TypeError("Введенная сумма должна быть типа int или float")
        if value < 0:
            raise ValueError("Введенная сумма должна положительным числом")


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
