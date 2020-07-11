# Probability of True Given a Positive Test Result



def prob_true_given_positive(p_true_prior,
                             false_positive_rate,
                             true_positive_rate):
    '''
    parameters:
          - probability of being true prior to test
          - false positive rate
          - true positive rate

    return:
          - the probability of being true given a positive test result
          - the number of tests to complete to be confident in the result
    '''
    probs = []
    complement = 1 - p_true_prior
    a = true_positive_rate*p_true_prior
    b = (true_positive_rate*p_true_prior) + (false_positive_rate*complement)
    posterior_probability = a/b
    sure = 1
    unsure = 0
    while unsure < sure:
        complement = 1 - posterior_probability
        probs.append(posterior_probability)
        if posterior_probability < 1:
            a = true_positive_rate*posterior_probability
            b = (true_positive_rate*posterior_probability) + (false_positive_rate*complement)
        posterior_probability = a/b
        unsure = round(posterior_probability, 2)
    print('Number of tests to complete:',
          len(probs), ',',
          'Test Results:',
          probs)
    return
