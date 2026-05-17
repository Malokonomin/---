import doctest


class Tree:
    def __init__(self, width: float, height: float):
        """
        Создание и подготовка к работе объекта "Дерево"
        :param width: Ширина дерева
        :param height: Высота дерева
        Примеры:
        >>> tree = Tree(2, 3)  # инициализация экземпляра класса
        """
        if not isinstance(width, (int, float)):
            raise TypeError("Ширина дерева должна быть типа int или float")
        if width <= 0:
            raise ValueError("Ширина дерева должна быть положительным числом")
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
        >>> tree = Tree(1, 1)
        >>> tree.is_small_Tree()
        True
        >>> tree = Tree(3, 5)
        >>> tree.is_small_Tree()
        False
        """
        return self.width < 2 and self.height < 3

    def chop_tree(self, hight: float) -> None:
        """
        Срубание дерева на указанную высоту.
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
        if hight > self.height:
            raise ValueError("Высота сруба не может превышать высоту дерева")
        self.height -= hight

    def strip_tree(self, estimate_width: float) -> float:
        """
        Снятие коры с дерева.
        :param estimate_width: Ширина снимаемой коры
        :raise ValueError: Если количество снимаемой коры превышает ширину дерева,
        то возвращается ошибка.
        :return: Объем реально снятой коры
        Примеры:
        >>> tree = Tree(2, 4)
        >>> tree.strip_tree(1)
        1.0
        """
        if not isinstance(estimate_width, (int, float)):
            raise TypeError("Ширина снимаемой коры должна быть типа int или float")
        if estimate_width < 0:
            raise ValueError("Ширина снимаемой коры должна быть положительным числом")
        if estimate_width > self.width:
            raise ValueError("Ширина снимаемой коры не может превышать ширину дерева")
        self.width -= estimate_width
        return float(estimate_width)


class Forest:
    def __init__(self, name: str):
        """
        Создание и подготовка к работе объекта "Лес"
        :param name: Название леса
        Примеры:
        >>> forest = Forest("Сосновый бор")
        """
        if not isinstance(name, str):
            raise TypeError("Название леса должно быть строкой")
        if len(name) == 0:
            raise ValueError("Название леса не может быть пустым")
        self.name = name
        self.trees = []

    def add_tree(self, tree: Tree) -> None:
        """
        Добавление дерева в лес.
        :param tree: Дерево для добавления
        Примеры:
        >>> forest = Forest("Дубрава")
        >>> tree = Tree(2, 3)
        >>> forest.add_tree(tree)
        """
        if not isinstance(tree, Tree):
            raise TypeError("В лес можно добавить только дерево")
        self.trees.append(tree)

    def count_small_trees(self) -> int:
        """
        Подсчет маленьких деревьев в лесу.
        :return: Количество маленьких деревьев
        Примеры:
        >>> forest = Forest("Березовая роща")
        >>> forest.add_tree(Tree(1, 1))
        >>> forest.add_tree(Tree(3, 5))
        >>> forest.add_tree(Tree(1, 2))
        >>> forest.count_small_trees()
        2
        """
        count = 0
        for tree in self.trees:
            if tree.is_small_Tree():
                count += 1
        return count


if __name__ == "__main__":
    doctest.testmod()