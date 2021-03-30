class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = firstname + ' ' + lastname
        self.wagers = []

    def __repr__(self): 
        return('Hello my name is {} {}'.format(self.firstname, self.lastname))


class Wager:
    def __init__(self, stake1, stake2):
        self.stake1 = stake1
        self.stake2 = stake2

    def __repr__(self): 
        return(f'{self.stake1} {self.stake2}')


if __name__ == '__main__':
    while True: 
        try:
            menu_selection = int(input(
'''
What would you like to do?
1. Create a person
2. Create a wager
3. View persons
4. View wagers
5. Exit

Enter your selection: 
'''
            ))
        except ValueError:
            continue
        else: 
            print(menu_selection)
            break


