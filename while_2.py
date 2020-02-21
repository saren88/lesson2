def ask_user():
    qa_dict = {'How you doing': 'Fine',
               'Who are you': 'Simple QA program',
               'What are you doing': 'Program',
               }

    while True:
        user_input = input('Ask me something(Example: how you doing,'
                           ' who are you, what are you doing): '
                           )
        for key, value in qa_dict.items():
            if user_input.lower() == qa_dict.get(key, value):
                print(value)
                break


ask_user()
