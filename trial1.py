import numpy as np
import pandas as pd
from hmmlearn import hmm

#path="/pb_winning_numbers.csv"
pb_data=pd.read_csv('data.csv')
model = hmm.GaussianHMM(n_components=69, covariance_type="full")
start=np.full((1,69),0.01492475362)
transition=np.full((69,69),0.01449275362)
emmision= np.identity(69)
model.startprob_ = start
model.transmat_ = transition
model.means_ =emmision