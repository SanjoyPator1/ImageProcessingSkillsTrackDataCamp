

test_labels = array([[0., 0., 1.],
       [0., 1., 0.],
       [0., 0., 1.],
       [0., 1., 0.],
       [0., 0., 1.],
       [0., 0., 1.],
       [0., 0., 1.],
       [0., 1., 0.]])

predictions = array([[0., 0., 1.],
       [0., 1., 0.],
       [0., 0., 1.],
       [1., 0., 0.],
       [0., 0., 1.],
       [1., 0., 0.],
       [0., 0., 1.],
       [0., 1., 0.]])




# Calculate the number of correct predictions
number_correct = (test_labels*predictions).sum()
print(number_correct)

# Calculate the proportion of correct predictions
proportion_correct = number_correct / (len(predictions))
print(proportion_correct)