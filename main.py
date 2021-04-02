class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = firstname + ' ' + lastname
        self.wagers = []

    def __repr__(self): 
        return('{} {}'.format(self.firstname, self.lastname))


class Wager:
    def __init__(self, stake1, stake2):
        self.stake1 = stake1
        self.stake2 = stake2

    def __repr__(self): 
        return(f'{self.stake1} {self.stake2}')

person_list = []

def show_main_menu(): 
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
            if menu_selection < 0 or menu_selection > 5:
                print('Invalid selection')
                continue
            else:
                selection(menu_selection)
                break

def selection(menu_selection):
    if menu_selection == 1: 
        create_person()
    elif menu_selection == 2:
        create_wager()
    elif menu_selection == 3: 
        list_person()
    else: 
        print(f'You selected {menu_selection}.')

def create_person(): 
    firstname = input('First Name: ').strip()
    lastname = input('Last Name: ').strip()
    new_person = Person(firstname, lastname)
    person_list.append(new_person)
    show_main_menu()

def create_wager():
    pass

def list_person(): 
    for number, person in enumerate(person_list, 1):
        print(number, person)
    show_main_menu()



if __name__ == '__main__':
    show_main_menu()

