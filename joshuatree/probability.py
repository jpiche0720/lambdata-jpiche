# Probability of True Given a Positive Test Result



def prob_true_given_positive(ptp, fpr, tpr, ci=0.99):
      '''
      Probability of True Given a Positive Test Result using Bayes Therom
      
      param:
            ptp :: probability of being true prior to test

            fpr :: false positive rate

            tpr :: true positive rate

            ci :: confidence interval (default .99)

      return:
            The test results for each test until desired confidence is reached. 
      '''
      probs = []
      complement = 1 - ptp
      a = tpr*ptp
      b = (tpr*ptp) + (fpr*complement)
      posterior_probability = a/b
      sure = ci
      unsure = 0
      while unsure < sure:
            complement = 1 - posterior_probability
            probs.append(posterior_probability)
            if posterior_probability < 1:
                  a = tpr*posterior_probability
                  b = (tpr*posterior_probability) + (fpr*complement)
            posterior_probability = a/b
            unsure = round(posterior_probability, 2)
      
      return probs
