import pickle
import pandas as pd
#from train import ohe
import numpy as np

model_file = 'house_price_model.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

house = {
'area'  :                   6540,
'bedrooms'  :                  3,
'bathrooms'  :                 1,
'stories'    :                 1,
'mainroad'   :                 1,
'guestroom'   :                1,
'basement'    :                1,
'hotwaterheating'  :           0,
'airconditioning'  :           0,
'parking'      :               2,
'prefarea'     :               1,
'furnishingstatus'  :  'furnished'
}

X = dv.transform([house])
y_pred = np.expm1(model.predict(X))

print('input', house)
print('predicted price:', y_pred)