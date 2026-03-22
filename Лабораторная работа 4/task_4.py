class Tree:
    def __init__(self, height: float, age: int):
        """
        Базовый класс дерева

        :param height: Высота дерева (в метрах)
        :param age: Возраст дерева (в годах)

        Примеры:
        >>> tree = Tree(5.5, 10)
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Высота должна быть числом")
        if height <= 0:
            raise ValueError("Высота должна быть положительной")
        self.height = float(height)

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть целым числом")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self.age = age

    def grow(self, meters: float):
        """
        Увеличивает высоту дерева

        :param meters: На сколько метров вырастет дерево

        Примеры:
        >>> tree = Tree(5.0, 10)
        >>> tree.grow(1.5)
        """
        if not isinstance(meters, (int, float)):
            raise TypeError("Рост должен быть числом")
        if meters <= 0:
            raise ValueError("Рост должен быть положительным")
        ...

    def get_info(self):
        """
        Возвращает информацию о дереве

        :return: Строка с информацией

        Примеры:
        >>> tree = Tree(5.0, 10)
        >>> tree.get_info()
        """
        ...

    def __str__(self):
        """
        Пользовательское представление

        Примеры:
        >>> tree = Tree(5.0, 10)
        >>> str(tree)
        'Дерево высотой 5.0 м'
        """
        return f"Дерево высотой {self.height} м"

    def __repr__(self):
        """
        Представление для разработчика

        Примеры:
        >>> tree = Tree(5.0, 10)
        >>> repr(tree)
        "Tree(height=5.0, age=10)"
        """
        return f"Tree(height={self.height}, age={self.age})"


class PineTree(Tree):
    def __init__(self, height: float, age: int, needle_length: float):
        """
        Сосна (дочерний класс)

        :param needle_length: Длина иголок (в см)

        Примеры:
        >>> pine = PineTree(6.0, 12, 5.5)
        """
        super().__init__(height, age)

        if not isinstance(needle_length, (int, float)):
            raise TypeError("Длина иголок должна быть числом")
        if needle_length <= 0:
            raise ValueError("Длина иголок должна быть положительной")
        self._needle_length = float(needle_length) # длинна иголок не меняется

    @property
    def needle_length(self):
        """Длина иголок"""
        return self._needle_length

    def grow(self, meters: float):
        """
        Перегруженный метод роста

        Причина перегрузки:
        Сосна растёт иначе, чем базовое дерево (имеет ограничения на рост за раз).

        :param meters: На сколько метров вырастет дерево

        Примеры:
        >>> pine = PineTree(6.0, 12, 5.5)
        >>> pine.grow(1.0)
        """
        if not isinstance(meters, (int, float)):
            raise TypeError("Рост должен быть числом")
        if meters <= 0:
            raise ValueError("Рост должен быть положительным")
        if meters > 2:
            raise ValueError("Сосна не может вырасти больше чем на 2 метра за раз")
        ...

    def drop_needles(self):
        """
        Сбрасывает иголки

        Примеры:
        >>> pine = PineTree(6.0, 12, 5.5)
        >>> pine.drop_needles()
        """
        ...

    def __repr__(self):
        """
        Перегружен, так как добавился новый атрибут

        Примеры:
        >>> pine = PineTree(6.0, 12, 5.5)
        >>> repr(pine)
        "PineTree(height=6.0, age=12, needle_length=5.5)"
        """
        return f"PineTree(height={self.height}, age={self.age}, needle_length={self.needle_length})"
if __name__ == "__main__":
    # Write your solution here
    pass
