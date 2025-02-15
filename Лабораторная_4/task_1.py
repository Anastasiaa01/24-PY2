# Write your solution here
class Rent:
    """Класс Аренда, расчитывает цену за аренду."""

    def __init__(self, day_price: (int, float), days: int) -> None:
        """Конструктор принимает цену аренды за 1 день и количество дней."""
        self.day_price = day_price
        self.days = days
        self.result = self.day_price * self.days

    def __str__(self) -> str:
        return f"Цена аренды за 1 день: {self.day_price}, количество дней: {self.days}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(day_price = {self.day_price}, days = {self.days})"

    def price(self) -> str:
        """Метод возвращает общую цену ареды."""
        return f"Цена аренды составит {self.result}"

    def discount(self, percent) -> str:
        """Метод для вычисления цены со скидкой."""
        discount_price = self.result - self.result * (percent / 100)
        return f"Цена аренды со скидкой {percent} процентов ставит {discount_price}"


class Hotel(Rent):
    """Класс Отель, расчитывает цену за аренду отеля."""

    def price(self) -> str:
        """Метод возвращает общую цену ареды.
        Цена аренды номера в отеле включает в себя цену за завтраки."""
        self.result = (self.day_price + 100) * self.days
        return f"Цена аренды составит {self.result}"


class Apartment(Rent):
    """Класс Апартаменты, расчитывает цену за аренду апартаментов."""

    def __init__(self, day_price: (int, float), days: int, age: int) -> None:
        """Конструктор принимает цену аренды за 1 день, количество дней и возраст съемщика."""
        self.age = age
        super().__init__(day_price, days)

    def __str__(self) -> str:
        return f"Цена аренды за 1 день: {self.day_price}, количество дней: {self.days}, возраст съёмщика: {self.age}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(day_price = {self.day_price}, days = {self.days}, age = {self.age})"

    def price(self) -> str:
        """Метод для вычисления цены со скидкой.
        При аренде апартаментов есть дополнительная скидка для детей и пенсионеров."""
        if self.age < 18 or self.age > 65:
            self.result = self.result - self.result * (10 / 100)
            return f"Цена аренды составит {self.result}"
        else:
            return f"Цена аренды составит {self.result}"


if __name__ == "__main__":
    u = Rent(1000, 2)
    print(u)
    print(repr(u))
    print(u.price())
    print(u.discount(15))
    print('____________________')
    a = Hotel(1000, 2)
    print(a)
    print(repr(a))
    print(a.price())
    print(a.discount(15))
    print('____________________')
    h = Apartment(1000, 2, 15)
    print(h)
    print(repr(h))
    print(h.price())
    print(h.discount(15))
