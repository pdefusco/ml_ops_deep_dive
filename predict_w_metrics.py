# Read the fitted model from the file model.pkl
# and define a function that uses the model to
# predict petal width from petal length

import pickle
import cdsw
import numpy

model = pickle.load(open('model.pkl', 'rb'))

@cdsw.model_metrics
def predict(args):
  
  cdsw.track_metric("input", args)
  petal_length = float(args.get('petal_length'))
  
  result = model.predict([[petal_length]])
  cdsw.track_metric("predict_result", result[0][0])
  modified_result = result+1
  cdsw.track_aggregate_metrics({"modified_result": agg_result}, start_timestamp_ms , end_timestamp_ms, model_deployment_crn=Deployment_CRN)
  return result[0][0]