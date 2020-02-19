user_age = input('How old are you? ')


def user_activity():
    if int(user_age) < 7:
        print('Now you are in kindergarten.')
    elif int(user_age) < 16:
        print('Now you are study in school.')
    elif int(user_age) < 22:
        print('Now you are study in university.')
    else:
        print('Now you are working.')


user_activity()
