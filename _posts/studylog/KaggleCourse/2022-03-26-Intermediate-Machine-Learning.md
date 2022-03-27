---
layout: post
title: Intermediate Machine Learning (from Kaggle Courses)
description: >
    None
# image: 
sitemap: false
categories:
  - studylog
  - kagglecourse
---

# Intermediate Machine Learning (from Kaggle Courses)

This is my study notes for [Intermediate Machine Learning in Kaggle Courses](https://www.kaggle.com/learn/intermediate-machine-learning)


## Missing Values

In real life Machine Learning model building process we rarely get clean dataset with every values in every rows and columns. Instead, we get datasets that are messy and has holes(missing values) in it. In this seciton we dive into methods on how to handle such mishaps in our datasets.

### Simply dropping the column or row with missing values

While this is the most intuitive and simplest way to manage missing values, we could potentially lose all the important features that are necessary in the model building process (i.e. removing `Number of Bathroom` column from housing price dataset)

### Imputation

Instead of dropping the entire row or column, we can fill in the missing value with some number. For example, we can insert the mean of the entire column into each missing data point. 

![Imputation](/assets/img/KaggleLearn/imputation.png){:.centered}

### Extension to Imputation

While imputation works well on some cases, it still doesn't capture the full essence of the dataset. The missing value could be significantly higher or lower than the imputed values. In order to increase the quality of the model (give more information to the model about the datset), we can add new column in the dataset that indicates whether certain column's value was missing or not. It is imporatnt to note that adding this new information (column) may or may not increase the quality of the model.

![ImputationExtension](/assets/img/KaggleLearn/imputation_extension.png){:.centered}

### Examples:

For this course, we will use the data from [Housing Prices Competition for Kaggle Learn Users](https://www.kaggle.com/c/home-data-for-ml-course)

The datset provided by kaggle is sperated into two dataset: train.csv and test.csv.

## Catergorical Variables

## Pipelines

## XGBoost

## Data Leakage

```python


```