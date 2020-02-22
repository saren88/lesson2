def stop_test():
    try:
        user_input = input('some ')
        print(user_input)
    except KeyboardInterrupt:
        print('\nbye')


stop_test()