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
