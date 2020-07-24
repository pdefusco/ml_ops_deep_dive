#remove this when possible
#!pip3 install scikit-learn

import pickle
import pandas as pd
import sklearn

model_dir = 'models/'
filename = 'finalized_model.sav'

data_dir = 'data/'

X = pd.read_csv(data_dir+'x.csv')
y = pd.read_csv(data_dir+'y.csv')

loaded_model = pickle.load(open(model_dir+filename, 'rb'))


def predict(data):
  
  header = ['col'+str(i) for i in range(X.shape[1])]
  df = pd.DataFrame(data, index=[0], columns=header)

  return {'result': loaded_model.predict(df)[0]}
