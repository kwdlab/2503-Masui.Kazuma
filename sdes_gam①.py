import math
import numpy as np
import pandas as pd
from tqdm import tqdm

#from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

from pygam import LinearGAM, s, te, f

from joblib import dump, load

import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='whitegrid')
sns.set_palette("bright")

from patsy import dmatrix

%matplotlib inline
%config InlineBackend.figure_format = 'retina'

column_names = ['cipher_left', 'cipher_right', 'plain_left', 'plain_right']
df = pd.read_csv('sdes_part1_new.csv',names=column_names)
print(df)

key = []
l = 0
for i in range(1024):
    for j in range(255):
        key.append(i)
        l += 1

X, y = df[column_names], key
df_data = pd.DataFrame(X, columns=column_names)

gam = LinearGAM(s(0) + s(1) + s(2) + s(3) , n_splines=35)

gam.fit(X_train, y_train)
gam.gridsearch(X_train, y_train)

gam.summary()

y_pred = gam.predict(X_test)

mae = np.mean(np.abs(y_test - y_pred))
print(mae)

rmse = math.sqrt(mean_squared_error(y_test, y_pred))
print(rmse)

grid_locs1 = [(0, 0), (0, 1),
              (1, 0), (1, 1)]
fig, ax = plt.subplots(2, 2, figsize=(15, 9))
for i, feature in enumerate(column_names):
    gl = grid_locs1[i]
    XX = gam.generate_X_grid(term=i)
    ax[gl[0], gl[1]].plot(XX[:, i], gam.partial_dependence(term=i, X=XX))
    ax[gl[0], gl[1]].plot(XX[:, i], gam.partial_dependence(term=i, X=XX, width=.95)[1], c='r', ls='--')
    ax[gl[0], gl[1]].set_xlabel('%s' % feature)
    ax[gl[0], gl[1]].set_ylabel('f ( %s )' % feature)