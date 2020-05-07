from bayes_proba_tester import prob_true_given_positive

print('hello')


x = float(input('p_true_prior'))
y = float(input('false_positive_rate'))
z = float(input('true_positive_rate'))
prob_true_given_positive(x,y,z)
