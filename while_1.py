def ask_user():

    while True:
        user_input = input('How you doing? ')
        if user_input.lower() == 'fine':
            print('I am happy for you.')
            break

ask_user()
