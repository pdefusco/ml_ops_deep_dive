#example from https://scikit-learn.org/stable/modules/ensemble.html#gradient-tree-boosting

from sklearn.datasets import make_hastie_10_2
from sklearn.ensemble import GradientBoostingClassifier
import pickle
import pandas as pd
import numpy as np

X, y = make_hastie_10_2(random_state=0)

X_train, X_test = X[:2000], X[2000:]
y_train, y_test = y[:2000], y[2000:]

clf = GradientBoostingClassifier(n_estimators=100, \
                                 learning_rate=1.0,max_depth=1, \
                                 random_state=0).fit(X_train, y_train)


#print(np.count_nonzero(X))
#print(X.shape)
#print(np.count_nonzero(~np.isnan(X)))

# save the model to disk
model_dir = 'models/'
filename = 'finalized_model.sav'
pickle.dump(clf, open(model_dir+filename, 'wb'))
  
# save data used for training
header = ['col'+str(i) for i in range(X.shape[1])]
data_dit = 'data/'
pd.DataFrame(X, columns=header).to_csv(data_dit+'x.csv', index=False)
pd.DataFrame(y).to_csv(data_dit+'y.csv', index=False)