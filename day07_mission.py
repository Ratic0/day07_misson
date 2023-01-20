#10.5
el_dict = {'name' : 'Hydrogen', 'symbol' : 'H', 'number' : 1}
class Element1():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
l = list(el_dict.values())

AA = Element1(l[0], l[1], l[2])
print(f'10.5 : {AA.name} ,{AA.symbol}, {AA.number}')



#10.6~7
class Element2():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(f'10.6 : {self.name}, {self.symbol}, {self.number}')

    def __str__(self):
        return f'10.7 : {self.name}, {self.symbol}, {self.number}'



hydrogen = Element2('Kim','K',2)
hydrogen.dump()
hydrogen2 = Element2('No','N','3')
print(hydrogen2)

#10.8