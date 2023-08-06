

class MyStack:

    def __init__(self):
        self.__stack = []

    # Добавление элемента в конец стэка
    def push(self, value):
        """Добавление элемента в стэк с конца"""
        self.__stack.append(value)

    # Удаляет последний элемент из стэка и возвращает его значение
    def pop(self):
        """Удаляет последний элемент из стэка и возвращает его значение"""
        return self.__stack.pop()

    # Возвращает значение последнего элемента стэка
    def peek(self):
        """Возвращает значение последнего элемента стэка"""
        if len(self.__stack) > 0:
            return self.__stack[-1]

    # Удаляет последнее значение из стэка
    def delete(self):
        """Удаляет последнее значение из стэка"""
        if len(self.__stack) > 0:
            self.__stack.pop()

    # Возвращает значение стэка
    def show(self):
        """Возвращает значение стэка"""
        code = ''
        for i in self.__stack:
            code += i + '\n'
        return code

    # Очищает стэк
    def clear(self):
        """Очищает стэк"""
        self.__stack = []

    # Возвращает значения всех элементов стэка (первый возвращаемый элемент = последний элемент стэка) и удаляет их
    def pop_all(self):
        """Возвращает значения всех элементов стэка (первый возвращаемый элемент = последний элемент стэка) и удаляет их"""
        result = []
        while len(self.__stack) != 0:
            result.append(self.__stack.pop())
        return result

    # Возвращает значения всех элементов стэка (первый возвращаемый элемент = последний элемент стэка)
    def peek_all(self):
        """Возвращает значения всех элементов стэка (первый возвращаемый элемент = последний элемент стэка)"""
        return [element for element in reversed(self.__stack)]

    # Возвращает значение элемента из стэка по индексу
    def __getitem__(self, item):
        """Возвращает значение элемента из стэка по индексу"""
        return self.__stack[item]

    # вызывает итерацию
    def __iter__(self):
        self.__iter_count = 0
        return self

    # передает значение в итератор перебирая элементы добавленные в стэк
    def __next__(self):
        if self.__iter_count < len(self.__stack):
            result = self.__stack[self.__iter_count-1]
            self.__iter_count += 1
            return result
        else:
            raise StopIteration
