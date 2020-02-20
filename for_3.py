school_data = [{'school_class': '1a', 'scores': [3, 5, 2, 4, 1, 4]},
               {'school_class': '2a', 'scores': [2, 5, 3, 4, 5, 5]},
               {'school_class': '3a', 'scores': [1, 3, 1, 3, 1, 4]},
               {'school_class': '4a', 'scores': [3, 4, 1, 2, 1, 5]}
               ]
scores_1a_sum = 0
for score in school_data[0]['scores']:
    scores_1a_sum += score

scores_1a_avg = scores_1a_sum / len(school_data[0]['scores'])

scores_2a_sum = 0
for score in school_data[1]['scores']:
    scores_2a_sum += score

scores_2a_avg = scores_2a_sum / len(school_data[1]['scores'])

scores_3a_sum = 0
for score in school_data[2]['scores']:
    scores_3a_sum += score

scores_3a_avg = scores_3a_sum / len(school_data[2]['scores'])

scores_4a_sum = 0
for score in school_data[3]['scores']:
    scores_4a_sum += score

scores_4a_avg = scores_4a_sum / len(school_data[3]['scores'])


print('Average school scores is: ' +
      str((scores_1a_avg +
           scores_2a_avg +
           scores_3a_avg +
           scores_4a_avg) /
          len(school_data)) + '.')
print('Average 1a scores is: ' + str(scores_1a_avg) + '.')
print('Average 2a scores is: ' + str(scores_2a_avg) + '.')
print('Average 3a scores is: ' + str(scores_3a_avg) + '.')
print('Average 4a scores is: ' + str(scores_4a_avg) + '.')
