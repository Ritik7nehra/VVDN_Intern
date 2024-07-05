# -*- coding: utf-8 -*-
"""Combined_Cycle_Power_Plant_Random_Forest_Reg.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/SantiagoMorenoV/Combined-Cycle-Power-Plant/blob/main/Models/Combined_Cycle_Power_Plant_Random_Forest_Reg.ipynb

# **Combined Cycle Power Plant - Random Forest Regression**

The "Combined Cycle Power Plant" dataset contains the following features (variables):

* **Temperature (T):** The temperature measured in °C.

* **Ambient Pressure (AP):** The ambient pressure measured in millibars.

* **Relative Humidity (RH):** The relative humidity measured in percent.

* **Exhaust Vacuum (V):** The exhaust vacuum measured in cm Hg.

* **Electrical Energy Output (EP):** The electrical energy output of the power plant measured in MW.

These features are used to estimate the electrical energy output of a combined cycle power plant. Each instance in the dataset represents a specific combination of these features and the corresponding electrical energy output.

For this purpose, I will estimate a *random forest regression* model and obtain its determination coefficient.

##Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

"""##Importing the dataset"""

dataset = pd.read_csv('https://raw.githubusercontent.com/SantiagoMorenoV/Combined-Cycle-Power-Plant/main/Data.csv')
X = dataset.iloc[:, :-1].values
y=  dataset.iloc[:, -1].values
dataset.head()

"""#**Descriptive Statistics**"""

print("\n\033[1m\033[36m\033[6m{:^50}\033[0m".format("Descriptive Statistics"))
print(dataset.describe())

"""##**Distributions and Boxplots**

## **Histograms**
"""

# Selecting our variables
variables = ["AT", "V", "AP", "AP", "PE"]

# Creating histograms
for var in variables:
  sns.histplot(data = dataset, x = var)
  plt.title("Histogram of {}".format(var))
  plt.show()

"""##**Boxplots**"""

# Creting Boxplots
for var in variables:
  sns.catplot(data=dataset, y = var, kind = "box", color = "#009E60")
  plt.title("{}'s Boxplot".format(var))
  plt.show()

"""##**Violin Plots**"""

# Creting Boxplots
for var in variables:
  sns.catplot(data=dataset, y = var, kind = "violin", color = "#009E60")
  plt.title("{}'s Violin Plot".format(var))
  plt.show()

"""#**Splitting the dataset into the Training and Test sets**"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state =0)

"""#**Training the Random Forest Regression model on the Training set**"""

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
regressor.fit(X_train, y_train)

"""#**Predicting the Test set results**"""

y_pred = regressor.predict(X_test)
np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

"""# **Evaluating the Model Performance**"""

from sklearn.metrics import r2_score
r2_score(y_test, y_pred)