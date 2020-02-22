def ask_user():

    qa_dict = {'how you doing': 'Fine',
                'who are you': 'Simple QA program',
                'what are you doing': 'Programming',
                }
    while True:
        try:
            user_input = input('Ask me something(Example: how you doing,'
                           ' who are you, what are you doing): '
                           )

            if user_input.lower() in qa_dict:
                print(qa_dict[user_input])
            elif user_input.lower() == 'end':
                break
        except KeyboardInterrupt:
            print('\nGoodbye')
            break


ask_user()