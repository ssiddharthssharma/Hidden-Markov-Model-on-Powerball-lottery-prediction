import numpy as np
import pandas as pd
from hmmlearn.hmm import MultinomialHMM

#path="/pb_winning_numbers.csv"
pb_data=pd.read_csv('data.csv')
start=np.full((1,69),0.01449275362)
transition=np.full((69,69),0.01449275362)
emmision= np.identity(69)
model = hmm.GaussianHMM(n_components=69, covariance_type="full")
model.startprob_ = start
model.transmat_ = transition
model.means_ = means
model.covars_ = covars
model.predict(X)