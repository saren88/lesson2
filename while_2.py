def ask_user():
<<<<<<< HEAD
    qa_dict = {'how you doing': 'Fine',
               'who are you': 'Simple QA program',
               'what are you doing': 'Programming',
=======
    qa_dict = {'How you doing': 'Fine',
               'Who are you': 'Simple QA program',
               'What are you doing': 'Program',
>>>>>>> 434867118f55644e0c0695eec227fd753e5e85ed
               }

    while True:
        user_input = input('Ask me something(Example: how you doing,'
                           ' who are you, what are you doing): '
                           )
<<<<<<< HEAD
        if user_input.lower() in qa_dict:
            print(qa_dict[user_input])
        elif user_input.lower() == 'end':
            break
=======
        for key, value in qa_dict.items():
            if user_input.lower() == qa_dict.get(key, value):
                print(value)
                break

>>>>>>> 434867118f55644e0c0695eec227fd753e5e85ed

ask_user()
