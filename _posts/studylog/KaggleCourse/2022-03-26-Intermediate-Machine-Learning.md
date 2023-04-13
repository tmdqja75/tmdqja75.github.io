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

This is my study notes for [Intermediate Machine Learning in Kaggle Courses](https://www.kaggle.com/learn/intermediate-machine-learning). All the images belongs to the course itself and are not produced by me.
{.:notes}

* this unordered seed list will be replaced by the toc
{:toc}

## Missing Values

In real life Machine Learning model building process we rarely get clean dataset with every values in every rows and columns. Instead, we get datasets that are messy and has holes(missing values) in it. In this seciton we dive into methods on how to handle such mishaps in our datasets.

### 1. Simply dropping the column or row with missing values

While this is the most intuitive and simplest way to manage missing values, we could potentially lose all the important features that are necessary in the model building process (i.e. removing `Number of Bathroom` column from housing price dataset)

### 2. Imputation

Instead of dropping the entire row or column, we can fill in the missing value with some number. For example, we can insert the mean of the entire column into each missing data point. 

![Imputation](/assets/img/KaggleLearn/imputation.png){:.centered}

### 3. Extension to Imputation

While imputation works well on some cases, it still doesn't capture the full essence of the dataset. The missing value could be significantly higher or lower than the imputed values. In order to increase the quality of the model (give more information to the model about the datset), we can add new column in the dataset that indicates whether certain column's value was missing or not. It is imporatnt to note that adding this new information (column) may or may not increase the quality of the model.

![ImputationExtension](/assets/img/KaggleLearn/imputation_extension.png){:.centered}

### Examples:

For this course, we will use the data from [Housing Prices Competition for Kaggle Learn Users](https://www.kaggle.com/c/home-data-for-ml-course)

The datset provided by kaggle is sperated into two dataset: train.csv and test.csv.

## Catergorical Variables

Sometimes, there are values in datasets that are not numerical values. Some values can be caterogrical, where each data is one of many different categories. There are three data preprocessing approach that we can use to deal with non-numerical categorical data. 

1. Drop Categorical Values
  
We can simply remove the columns that contains categorical values if such columns are not important factors in the dataset

2. Ordinal Encoding

Ordinal encoding assigns each values in category to a unique numerical value.

![OrdinalEncoding](/assets/img/KaggleLearn/ordinalEncoding.png)

Ordinal encoding works well with ordinal variables. **Ordinal varibles** are values with clear ordering such as satisfaction rate (Satisfies, Neutral, Unsatisfied) or member status (Gold, Silver, Bronze). 

3. One-Hot Encoding

One-hot encoding adds new amount of columns same as the number of values in the category.

![One Hot Encoding](/assets/img/KaggleLearn/oneHotEncoding.png)

One-hot encoding does not assume an ordering of the values in the category. (These are called **nominal variables**). One-hot encoding generally does not perform well if the number of values in the category takes on large amount of number. Generally, one-hot encoding won't be used if the number of values in the category exceeds 15 values.

## Pipelines

Pipelines module provides cleaner and more organized data preprocessing and modeling coding. It bundles several preprocessing and modeling steps so the developer can process data with easier and intuitive code. 

Pipeline has several benefits, including:
1. Cleaner code
2. Fewer bugs
3. Easier to productionize
4. More ofption for model validation

[One Hot Encoding](/assets/img/KaggleLearn/oneHotEncoding.png)

## Cross Validation
Cross validation divides original training dataset into eqally distributed k amount of sets (If $k=5$, 20 percent of data will be in each division). Each division is called '**folds**'. In each experiment the first fold is held as validation set, and the model is traind with rest of four folds dataset. The experiment repeats with until we reach to the last fold. This validation process is also known as k-fold validation. 

Given that the model is trained several time, with large dataset, the whole validation process could take a lot of time. It is important to acknowledge these tradeoff. 
- for small enough dataset, it is ok to run several cross-validation
- for large datasets, one should consider running only few cross-validation.



