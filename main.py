# isEmpty - проверка стека на пустоту. Метод возвращает True или False.
# push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
# pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
# peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
# size - возвращает количество элементов в стеке.
from collections import Counter


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


PAIRS_OF_BRACKETS = ('()', '[]', '{}')

stack = Stack()


def check(string):
    for char in string:
        if char in '([{':
            stack.push(char)
        else:
            if stack.isEmpty():
                return False
            else:
                if stack.peek() + char in PAIRS_OF_BRACKETS:
                    stack.pop()
                else:
                    return False

    return stack.isEmpty() or False


print(check('(((([{}]))))'))
print(check('[([])((([[[]]])))]{()}'))
print(check('{{[()]}}'))
print(check('}{}'))
print(check('{{[(])]}}'))
print(check('[[{())}]'))
