#remove this when possible
#!pip3 install scikit-learn

import pickle
import pandas as pd
import sklearn
import cdsw

model_dir = 'models/'
filename = 'finalized_model.sav'

data_dir = 'data/'

X = pd.read_csv(data_dir+'x.csv')
y = pd.read_csv(data_dir+'y.csv')


loaded_model = pickle.load(open(model_dir+filename, 'rb'))

# Adding the decorator to track each prediction
# Each prediction is assigned a UUID

@cdsw.model_metrics
def predict(data):
  
  header = ['col'+str(i) for i in range(X.shape[1])]
  df = pd.DataFrame(data, index=[0], columns=header)

  return {'result': loaded_model.predict(df)[0]}
