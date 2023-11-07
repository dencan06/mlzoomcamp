# basic
import pandas as pd
import numpy as np

# viz
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display

# sklearn
from sklearn import preprocessing
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge, RidgeCV, Lasso, LassoCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import roc_auc_score, mean_squared_error

#loading
import pickle


df = pd.read_csv('Housing_prices.csv')

df = df.replace({'yes': 1, 'no': 0})
cat = df.iloc[:,1:].to_dict(orient='records')
dv = DictVectorizer(sparse=False)
dv.fit(cat)
X_dict = dv.transform(cat)
df['log_price'] = np.log1p(df.price)
Y = df.log_price

print("Training the model")

X_train_full, X_test, Y_train_full, Y_test = train_test_split(X_dict,Y, test_size=0.2, random_state=2)

rf = RandomForestRegressor(n_estimators=200, max_depth=15, min_samples_leaf=3, random_state=1)
rf.fit(X_train_full, Y_train_full)

y_pred = rf.predict(X_test)
print(f'test rmse:{np.sqrt(mean_squared_error(Y_test, y_pred)):.5f}')

with open ('house_price_model.bin', 'wb') as f:
    pickle.dump((dv, rf), f)

print("Model training completed, model is saved to 'house_price_model.bin'")

