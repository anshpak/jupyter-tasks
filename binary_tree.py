class BinaryTree:
    """
    Класс BinaryTree, отвечающий за проектирование бинарного дерева поиска.
    
    Методы:
    __init__, __repr__(self), insert(self, value), __contains__(self, value), __len__(self), lcr(self), min(self), max(self),
    """
    
    def __init__(self):
        """
        Метод перегружает встроенную функцию init; возвращает экземпляр объекта типа EmptyNode, создает бинарное дерево поиска без вершин.
        """
        self.root = EmptyNode()
    
    def __repr__(self):
        """
        Метод перегружает встроенную функцию repr; возвращает строковый объект - представление бинарного дерева поиска в интерактивной ячейке.
        """
        return repr(self.root)
    
    def insert(self, value):
        """
            Метод вставки элемента в бинарное дерево поиска.
        """
        self.root = self.root.insert(value)
        
    def __contains__(self, value):
        """
        Метод перегружает встроенную функцию in; возвращает булевское значение True или False в зависимости от результат проверки вхождения в дерево переданного значения value.
        """
        return value in self.root
    
    def __len__(self):
        """
        Метод перегружает встроенную функцию len; возвращает текущую длину бинарного дерева поиска (количество вершин).
        """
        return len(self.root)
    
    def lcr(self):
        """
        Центрированный обход дерева. Метод возвращает осортированный список значений бинарного дерева.
        """
        return self.root.lcr()
    
    def min(self):
        """
        Метод возвращает минимальное значение в бинарном дереве поиска. Основан на центрированном обходе дерева.
        """
        return self.root.min()
    
    def max(self):
        """
        Метод возвращает максимальное значение в бинарном дереве поиска. Основан на центрированном обходе дерева.
        """
        return self.root.max()
    
class EmptyNode:
    """
    Вспомогательный класс EmptyNode, отвечающий за проектирование пустого элемента бинарного дерева поиска.
    
    Методы:
    __repr__(self), insert(self, value), __contains__(self, value), __len__(self), lcr(self), min(self), max(self),
    """
    
    def __repr__(self):
        """
        Метод перегружает встроенную функцию repr; возвращает символ '*', представление пустой вершины.
        """
        return "*"
    
    def insert(self, value):
        """
        Метод вставки элемента в бинарное дерево поиска, инструкции вершине. Возвращает экземпляр класса BinaryNode.
        """
        return BinaryNode(self, value, self)
    
    def __contains__(self, value):
        """
        Метод перегружает встроенную функцию in; возвращает булевское значение False: переданное значение value не входит в бинарное дерево поиска.
        """
        return False
    
    def __len__(self):
        """
        Метод перегружает встроенную функцию len; возвращает текущую длину бинарного дерева поиска (количество вершин), равную нулю.
        """
        return 0
    
    def lcr(self):
        """
        Метод возвращает пустой список.
        """
        return []
    
    def min(self):
        """
        Метод возвращает None.
        """
        return None
    
    def max(self):
        """
        Метод возвращает None.
        """
        return None
    
class BinaryNode():
    """
    Вспомогательный класс BinaryNode, отвечающий за проетирование элементов бинарного дерева поиска (вершин).
    
    Атрибуты: 
    count: атрибут класса BinaryNode, которого нет в экземплярах класса; счетчик количества элементов бинарного дерева поиска, по умолчанию равный нулю. Увеличивается на один с каждым добавлением новой вершины.
    left: атрибут, указывающий на левое поддерево текущего элемента (вершины); содержит экземпляр класса BinaryNode или EmptyNode.
    value: атрибут, хранящий текущее значение элемента (вершины).
    right: атрибут, указывающий на правое поддерево текущего элемента (вершины); содержит экземпляр класса BinaryNode или EmptyNode.
    
    Методы:
    __init__, __repr__(self), insert(self, value), __contains__(self, value), __len__(self), lcr(self), min(self), max(self),
    """
    
    count = 0
    
    def __init__(self, left, value, right):
        """
        Метод перегружает встроенную функцию init; возвращает экземпляр объекта типа BinaryNode, создает вершину бинарного дерева поиска, присваивая значения left, value, right соответствующим атрибутам.
        """
        self.left = left
        self.value = value
        self.right = right
        BinaryNode.count += 1
        
    def __repr__(self):
        """
        Метод перегружает встроенную функцию repr; возвращает строку - представление вершины бинарного дерева поиска.
        """
        return "(%s, %s, %s)" % (repr(self.left), repr(self.value), repr(self.right))
    
    def insert(self, value):
        """
        Метод вставки элемента в бинарное дерево поиска, инструкции вершине. Если переданное значение value меньше значения self.value текущей вершины, левой вершине текущей вершины присваивается результат выполнения метода вставки, вызванного из левой вершины текущей вершины; иначе правой вершине текущей вершины присваивается результат выполнения метода вставки, вызванного из правой вершины текущей вершины. В конце возвращается текущая вершина для того, чтобы рекурсивно быть присвоенной атрибуту экземпляра left или right, из которого была вызвана.
        """
        if value < self.value:
            self.left = self.left.insert(value)
        else:
            self.right = self.right.insert(value)
        return self
    
    def __contains__(self, value):
        """
        Метод перегружает встроенную функцию in; возвращает булевское значение True, если переданное значение value совпадает с значением self.value текущей вершины; иначе если переданное значение value меньше значением self.value текщей вершины, то проверка продолжается в левом поддереве; иначе проверка продолжается в правом поддереве.
        """
        if value == self.value:
            return True
        elif value < self.value:
            return value in self.left
        else:
            return value in self.right
        
    def __len__(self):
        """
        Метод перегружает встроенную функцию len; возвращает текущее значение атрибута count объекта класса BinaryNode - текущую длину бинарного дерева поиска (количество вершин).
        """
        return self.count
    
    def lcr(self):
        """
        Центрированный обход дерева, инструкции в вершине. Метод рекурсивно возвращает список значений вершин в бинарном дереве поиска: заходит сначала в левое поддерево, потом возвращает вершину, а потом заходит в правое поддерево.
        """
        result = []
        result += self.left.lcr() + [self.value]
        result += self.right.lcr()
        return result
    
    def min(self):
        """
        Метод возвращает значение текущей вершины в бинарном дереве поиска, если левое поддерево текущей вершины является экземпляром класса EmptyNode; иначе поиск минимального значения продолжается в левом поддереве рекурсивно.
        """
        if isinstance(self.left, EmptyNode):
            return self.value
        else:
            return self.left.min()
        
    def max(self):
        """
        Метод возвращает значение текущей вершины в бинарном дереве поиска, если правое поддерево текущей вершины является экземпляром класса EmptyNode; иначе поиск максимального значения продолжается в правом поддереве рекурсивно.
        """
        if isinstance(self.right, EmptyNode):
            return self.value
        else:
            return self.right.max()