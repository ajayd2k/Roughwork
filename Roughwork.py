num = int(input('Enter a number greater than 5 : '))
try:
    assert num>=5, 'The number entered by you is not greater than 5'
    print('The number greater than 5 entered by you is :', num)
except AssertionError:
    print('The Entered number by you is not greater than 5. Please re-enter the number.')



