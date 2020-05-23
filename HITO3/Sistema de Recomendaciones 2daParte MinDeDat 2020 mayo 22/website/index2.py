from flask import Flask, render_template

app = Flask(__name__)

import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import sklearn
df_users = pd.read_csv("users.csv")
df_repos = pd.read_csv("repos.csv")
df_ratings = pd.read_csv("ratings.csv")
df_users.head()
df_repos.head()
df_ratings.head()
n_users = df_ratings.userId.unique().shape[0]
n_items = df_ratings.repoId.unique().shape[0]
print (str(n_users) + ' users')
print (str(n_items) + ' items')
plt.hist(df_ratings.rating,bins=8)

# Make sure this we are executing this file
if __name__ == '__main__':
    app.run(debug=True)
