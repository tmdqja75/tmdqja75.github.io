---
layout: post
title: Introduction to Machine Learning (from Kaggle Courses)
description: >
    None
# image: https://www.kaggle.com/static/images/education/km/learn-home-208h@2x.png
sitemap: false
categories:
  - studylog
  - kagglecourse
---
# Introduction to Machine Learning (from Kaggle Courses)

* this unordered seed list will be replaced by the toc
{:toc}

## How Models Work
Most machine learning models are based on the **training data**, which is data provided by the user. Whatever form of models you are using, the model receives loads of training data and try to find the patterns among the given data. This step is called **fitting** or **training** the model. 

After the model finishes its training, it can be used to **predict** values for the new given dataset that wasn't included in the original training dataset. 

## Basic Data Exploration

Kaggle ML introductory course uses Iowa housing price dataset to predict the price of new houses in real estate. Also, the imported dataset will be managed by the famous python dataset library called `pandas`.

To import pandas in python, you need to use following command

```python
import pandas as pd
```

`pandas` library can read csv file and convert it into `pandas`' own dataFrame

```python
iowa_data = pd.read_csv('/iowa_data.csv')
iowa_data.describe()
```
![iowa_data](/assets/img/KaggleLearn/iowa_data_describe.png)

`df.describe()` displays descriptive statistics of each features in given dataFrame `df`. 
- `mean`: average of a feature
- `std`: standard deviation of a feature (how spread out the values are)
- `min`: minimum value in a feature
- `max`: maximum value in a feature
- `25%`, `50%`, `75%`: 25th, 50th, 75th percentile of values in a feature
	


## First Machine Learning Model

### Features and Prediction target

To start building and training the model, we first need to select which features our model should depend on. By intuition, we know that features such as door color are less significat in housing price than number of rooms or number of floors. 

From the dataFrame we made above (`iowa_data`), we need to select the prediction target (conventionaly stored as `y`) and the relavant **features** (conventionally stored as `X`).

The prediction target columns can be selected with pandas' **dot notation**.

```python
y = iowa_data.Price
```

The features can be selected with the list of features columns names

```python
iowa_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = iowa_data[iowa_features]
```

### Building a Model

Typical steps of building and utilizing the model is as follows:
- **Define**: What type of model will you use? (decision tree?, SVM?)
- **Fit**: train the selected model with your own dataset
- **Predict**: input new data into trained model
- **Evaluate**: check if the model's output is accurate or not

To build a model that predicts a housing price, we will use Decision Tree model on our prepared dataset (`X,` `y`). python library `scikit-learn` contains `DecisionTreeRegressor` method that we can use to train ML model. Here

```python
from sklearn.tree import DecisionTreeRegressor
iowa_model = DecisionTreeRegressor(random_state=1)
iowa_model.fit(X, y)
```

The code above calls and set `DecisionTreeRegerssor` model to `iowa_model` and fit `X` and `y` to the model.

To make prediction you would use `predict` command on `X`. 

```python
prediciton = iowa_model.predict(X)
print(prediction)
```

```
[208500. 181500. 223500. ... 266500. 142125. 147500.]
```


## Model Validation

Before checking the validation of the model, we first introduce one of many metrics that represents the model quality.

### MAE (Mean Absolute Error)

MAE is mean value of all absolue values of errors
$$error = actual-predicted$$

$$\sum_{i=1}^{n}{|{error}|_i}/n$$

In laymen's term, it means that "On average, the predicitons are off by about this much".

`sklearn` library comes with its own mean absolute error function

```python
from sklearn.metrics import mean_absolute_error
predicted_home_prices = iowa_model.predict(X)
mean_absolute_error(y, predicted_home_prices)
```

```
434.71593042
```

Intuitively, however, using the feature dataset `X` in our validation doesn't seem like the ideal way to proove the credibility of our model. It's like a professor giving out same midterm (`X`) to same group of students (`model`) over and over. In order to rigorously proove our model, we need to use new datasets that was never used in the process of training the model. This new dataset that the model has never seen before is called the **validaiton data**.

With no surprise, `scikit-learn` library comes with a method that splits feature set (`X`) into training data and validation data. This

```python
from sklearn.model_selection import train_test_split

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)
# train model just with train dataset
iowa_model = DecisionTreeRegressor()
iowa_model.fit(train_X, train_y)
```

Let's check the MAE of the model using validation dataset

```python
val_predictions = iowa_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))
```

```
258930.02343245
```

We can see that MAE calculated with data inside training `X` dataset and the one with validation `X` dataset are significantly different; the MAE of validation dataset is way highter. This shows that the model ww've build with decision tree is impractical to use in actual prediction

## Underfitting and Overfitting



## Random Forest

## Machine Learning Competition