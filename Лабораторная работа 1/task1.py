import doctest


class Tree:
    def __init__(self, width: float, height: float):
        """
        Создание и подготовка к работе объекта "Стакан"

        :param capacity_volume: Ширина дерева
        :param occupied_volume: Высота дерева

        Примеры:
        >>> tree = Tree(2, 3)  # инициализация экземпляра класса
        """
        if not isinstance(width, (int, float)):
            raise TypeError("Ширина дерева должена быть типа int или float")
        if width <= 0:
            raise ValueError("Ширина дерева должен быть положительным числом")
        self.width = width

        if not isinstance(height, (int, float)):
            raise TypeError("Высота должна быть int или float")
        if height < 0:
            raise ValueError("Высота не может быть отрицательным числом")
        self.height = height

    def is_small_Tree(self) -> bool:
        """
        Функция которая проверяет является ли дерево маленьким

        :return: Является ли дерево маленьким

        Примеры:
        >>> tree = Tree(<1, <2)
        >>> tree.is_small_Tree()
        """
        ...


    def chop_tree(self, hight: float) -> None:
        """
        Добавление высоты дереву.
        :param hight: Высота сруба

        :raise ValueError: Если количество высоты сруба больше высоты дерева добавляем ошибку

        Примеры:
        >>> tree = Tree(2, 4)
        >>> tree.chop_tree(3)
        """
        if not isinstance(hight, (int, float)):
            raise TypeError("Высота сруба должна быть типа int или float")
        if hight < 0:
            raise ValueError("Высота сруба должна положительным числом")
        ...

    def strip_tree(self, estimate_width: float) -> None:
        """
        Извлечение воды из стакана.

        :param estimate_width: Ширина снимаемой коры
        :raise ValueError: Если количество снимаемой коры превышает ширину дерева,
        то возвращается ошибка.

        :return: Объем реально снятой коры

        Примеры:
        >>> tree = Tree(2, 4)
        >>> tree.strip_tree(1)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации