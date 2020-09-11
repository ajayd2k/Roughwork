num = int(input('Enter a number greater than 5 : '))
try:
    assert num>=5, 'The number entered by you is not greater than 5'
    print('The number greater than 5 entered by you is :', num)
except AssertionError:
    print('The Entered number by you is not greater than 5. Please re-enter the number.')





# Code for finding highest Even number in a given list

def highest_even(li):
    Highest = 0
    for item in li:
        if item % 2 == 0:
            if item > Highest:
                Highest = item
    return Highest


print (highest_even ([21, 22, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))

# Programme to find the highest number input by the user.
num = int (input ('Enter a number greater than 5 : '))
try:
    assert num >= 5, 'The number entered by you is not greater than 5'
    print ('The number greater than 5 entered by you is :', num)
except AssertionError:
    print ('The Entered number by you is not greater than 5. Please re-enter the number.')


#
num = [-5,4,3,2,1,0,-1,-2,-3,-4,-5]
for i in num:
    if(i<0):
        print(i)
    else :
        continue

# Classes
class PlayerCharacter:
    membership = True # Class Attribute which are static
    def __init__(self, name, age):
        if (age > 18):
            self.name = name #Declared Attribute which are dynamic
            self.age = age #Declared Attribute which are dynamic

    def run(self):#Method in a class
        print ('run')#Method in the class but the return is not defined and hence it will print run and then none because the return is none.



player1 = PlayerCharacter ('Ajay', 24) #Instantiate the class / Creating an object with the details mentioned.
player2 = PlayerCharacter ('Shital', 45) #Instantiate the class / Creating an object with the details mentioned.
player2.attack = '50' #adding of an attribute to the object
player1.membership = False #Changing the Class Attribute values

print (player2.name, player2.age)
print (f'My Name is {player1.name} and I am {player1.age} years old.')
print (player1.name, player1.age)
print(player2.attack)
print(player1.membership)
print(player1.name,player1.run())
print(player2.name,player2.run())

