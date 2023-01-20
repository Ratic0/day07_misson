#10.1
class Thing:
    def ex(self):
        return self

example = Thing()
print(Thing)
print(example)

#10.2

class Thing2:
    def __init__(self):
        self.letters = 'abc'
    def outing(self):
        print(self.letters)

A = Thing2()
A.outing()

#10.3
class Thing3:
    def __init__(self):
        self.letters = 0

B=Thing3()
B.letters = 'xyz'
print(B.letters)

#10.4
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
C = Element
C.name = 'Hydrogen'
C.symbol = 'H'
C.number = 1
print(f'{C.name}, {C.symbol}, {C.number}')








