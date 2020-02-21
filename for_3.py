school_data = [{'school_class': '1', 'scores': [3, 5, 2, 4, 1, 4]},
               {'school_class': '2', 'scores': [2, 5, 3, 4, 5, 5]},
               {'school_class': '3', 'scores': [1, 3, 1, 3, 1, 4]},
               {'school_class': '4', 'scores': [3, 4, 1, 2, 1, 5]}
               ]
avg_school_score = 0
school_scores = 0
for school_class_data in school_data:
    scores_class = 0
    avg_class_score = 0
    for score in school_class_data['scores']:
        scores_class += score
        avg_class_score = scores_class / len(school_class_data['scores'])
    print('Average score in ' + str(school_class_data['school_class']) +
          ' class is: ' + str(avg_class_score) + '.')
    school_scores += avg_class_score
    avg_school_score = school_scores / len(school_data)
print('Average school scores is: ' + str(avg_school_score) + '.')

