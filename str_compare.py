def str_compare():
    first_str = str(input('Please enter something: '))
    second_str = str(input('Please enter something one more time: '))

    if type(first_str) == str and type(second_str) == str:
        print(0)
    elif first_str == second_str:
        print(1)
    elif first_str != second_str and len(str(first_str)) > len(str(second_str)):
        print(2)
    elif first_str != second_str and second_str == 'learn':
        print(3)


str_compare()
