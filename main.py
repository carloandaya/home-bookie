class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = firstname + ' ' + lastname

    def __str__(self): 
        return('Hello my name is {} {}'.format(self.firstname, self.lastname))

    def sayHello(self): 
        print('Hello world!')
        
class Wager:
    def __init__(self, party1: Person, party2: Person, amount):
        self.party1 = party1
        self.party2 = party2
        self.amount = amount

    def __str__(self):
        return('Wager between {} and {} for {}'.format(self.party1.fullname, self.party2.fullname, self.amount)) 



p = Person('Bart', 'Simpson')
me = Person('Carlo', 'Andaya')
w = Wager(p, me, 150)

print(w)


