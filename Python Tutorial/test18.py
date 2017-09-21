def my_divide(x, y):
    try:
        x / y
    except ZeroDivisionError:
        print('Error: zero division')
    else:
        print('Result: ' + str(x/y) + ' (without error)')
    finally:
        print('Done')

my_divide(10,5)
my_divide(10,0)

