


def fibonacci(n):
    if n < 1 or int(n) != n:
        return "error, n should be a positive number which is greater than 1"
    if n < 3:
        return 1
    a, b = 1, 1

    for i in range(2, n):
        a = a + b if i % 2 == 0 else a
        b = a + b if i % 2 == 1 else b
    return a if a > b else b


def fibonacci_list(n):
    if n < 1 or int(n) != n:
        return "error, n should be a positive number which is greater than 1"
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    list = [1, 1]
    for i in range(2, n):
        list.append(list[i-2]+list[i-1])
    return list

class Queue():
    def __init__(self):
        self.__queue = []

    def show(self):
        print(self.__queue)

    def add(self,content):
        try:
            self.__queue.append(content)
        except:
            print('invalid input')

    def pop(self):
        try:
            del self.__queue[0]
        except IndexError:
            print('warning : no value in the queue,try add(content) to add one')

class Stack():
    def __init__(self):
        self.__stack = []

    def show(self):
        print(self.__stack)

    def add(self,content):
        try:
            self.__stack.insert(0,content)
        except:
            print('invalid input')

    def pop(self):
        try:
            del self.__stack[0]
        except IndexError:
            print('warning : no value in the stack,try add(content) to add one')






