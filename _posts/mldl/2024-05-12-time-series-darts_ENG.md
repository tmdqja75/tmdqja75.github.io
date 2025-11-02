---
layout: post
title: Time Series Data Package - Darts
description: >
  A comprehensive and user-friendly approach in Python for modeling and forecasting various time series data.
image: https://unit8.com/wp-content/uploads/2021/07/darts-time-series-made-easy-in-python.png
categories: mldl
sitemap:
    changefreq : weekly
comments: true
---

* This list will be replaced by the table of contents
{:toc}

# Effortlessly Forecasting Time Series Data with Darts

Time series data plays a crucial role in many fields. Analyzing and predicting time series data across various domains such as finance, weather, production, and health aids in making informed decisions. To facilitate such tasks, Python offers a variety of libraries.

One of these standout libraries is Darts. As its name suggests, Darts is a robust tool for handling and forecasting time series data in Python. Developed by Unit8, a Swiss company, this library is user-friendly and supports a range of models, allowing for flexible adaptation to different types of time series data.

## Key Features of Darts

Darts provides several functionalities related to time series. The following diagram illustrates various time series-related features offered by Darts.

![darts_function](https://unit8.com/wp-content/uploads/2021/07/1_yaHh5V0AgxEYxJYrv9VQmA.png)

1. **Time Series Modeling**: Darts offers a variety of time series models, including ARIMA, Prophet, RNN, LSTM, and TCN, enabling users to choose the most suitable model for their data.

2. **Time Series Forecasting**: With Darts, you can predict future values of time series data while also considering the uncertainty of predictions by providing confidence intervals.

3. **Time Series Data Preprocessing**: Darts offers numerous functions to preprocess and transform data, preparing it before modeling. This includes normalization, handling missing values, and detecting outliers.

4. **Time Series Decomposition**: Darts can decompose time series data into trend, seasonality, and residuals, allowing for a better understanding of patterns within the data and improving forecasting models.

5. **Validation and Evaluation**: Darts provides various tools to assess and validate model performance, enabling you to evaluate and enhance predictive capabilities.

In this post, we will explore how to visualize and preprocess time series data easily using Darts and how to create a pipeline to experiment with different models.

## Visualizing/Preprocessing Time Series Data with Darts

### Data

- First, we will utilize one of the example time series datasets provided by Darts for demonstration.
- In this post, we will work with the monthly milk sales dataset (`MonthlyMilkIncompleteDataset`).
- Darts handles all time series data as `TimeSeries` objects.

```python
from darts.datasets import MonthlyMilkIncompleteDataset
import matplotlib.pyplot as plt
series = MonthlyMilkIncompleteDataset().load()

plt.figure(figsize=(16, 3))
series.plot();
```

![png](/assets/img/2024-05-12-time-series-darts_files/2024-05-12-time-series-darts_4_0.png)

### Scaler
- You can easily scale your time series dataset using the Scaler class provided by Darts.
- The default Scaler is MinMaxScaler, but you can use other scaling preprocessing methods as well (e.g., StandardScaler).
- It operates similarly to scikit-learn's API, allowing you to `fit` the Scaler and `transform` the actual time series data.
- You can reconstruct the original data from the scaled data using the `inverse_transform` function.

```python
from darts.dataprocessing.transformers import Scaler

scaler = Scaler()
rescaled = scaler.fit_transform(series)

plt.figure(figsize=(16, 3))
rescaled.plot();
```

![png](/assets/img/2024-05-12-time-series-darts_files/2024-05-12-time-series-darts_6_0.png)

```python
back = scaler.inverse_transform(rescaled)

plt.figure(figsize=(16, 3))
back.plot();
```

![png](/assets/img/2024-05-12-time-series-darts_files/2024-05-12-time-series-darts_7_0.png)

### Filling Missing Values
- When handling time series data, it is common to encounter many missing values. 
- You can interpolate these missing data points in various ways using the `MissingValuesFiller` class.

```python
from darts.dataprocessing.transformers import MissingValuesFiller # type: ignore
series_missing = series.copy()

plt.figure(figsize=(16, 3))
series_missing.plot();
```

![png](/assets/img/2024-05-12-time-series-darts_files/2024-05-12-time-series-darts_9_0.png)

```python
filler = MissingValuesFiller()
filled_linear = filler.transform(series_missing, method="linear")
filled_quadratic = filler.transform(series_missing, method="quadratic")

plt.figure(figsize=(16, 3))
filled_linear.plot(label='filled_linear')
filled_quadratic.plot(label='filled_quadratic')
series_missing.plot(label='original');
```

![png](/assets/img/2024-05-12-time-series-darts_files/2024-05-12-time-series-darts_10_0.png)

### Pipeline
- When preprocessing time series data, it is common to employ numerous preprocessing methods.
- As the number of preprocessing methods increases, managing the associated classes and variables can become challenging, complicating the process of deploying the same preprocessing environment.
- To make this easier, Darts offers a `Pipeline` feature similar to scikit-learn.

```python
from darts.dataprocessing import Pipeline

incomplete_series = series.copy()

# Instantiate classes needed for data preprocessing
filler = MissingValuesFiller()
scaler = Scaler()

# Create a Pipeline
pipeline = Pipeline([filler, scaler])
transformed = pipeline.fit_transform(incomplete_series)

plt.figure(figsize=(16, 3))
transformed.plot();
```

![png](/assets/img/2024-05-12-time-series-darts_files/2024-05-12-time-series-darts_12_0.png)

- If all the functionalities within the Pipeline can perform inverse_transform, the Pipeline itself can also do so. 
- If any functionality within the Pipeline does not support inverse_transform (e.g., `MissingValuesFiller`), you can configure it to exclude that functionality by setting `partial=True`.

```python
back = pipeline.inverse_transform(transformed, partial=True)

plt.figure(figsize=(16, 3))
back.plot();
```

![png](/assets/img/2024-05-12-time-series-darts_files/2024-05-12-time-series-darts_14_0.png)

- Before moving on to the next step, Darts deep learning models require the data to be in the `float32` data type, so we will convert the transformed data accordingly.

```python
import numpy as np
transformed = transformed.astype(np.float32)
```

## Training Models with Preprocessed Data
- With the training data fully prepared, it’s time to set up the model.
- Darts offers a variety of models, from simple statistical ones to complex deep learning models (from ARIMA to PyTorch Forecast).
- You can check out all the models provided by Darts at [this link](https://unit8co.github.io/darts/README.html#forecasting-models).

### Darts Model Training Process
- When a model is trained in Darts, it follows this process:

![darts_train](https://unit8co.github.io/darts/_images/seq_dataset_one_ts.png)

- **Input Data**: The model slices the input data from the beginning up to the specified size (`input_chunk_length`). It shifts one step at a time to slice the next chunk (T0 ~ T3 / T1 ~ T4 / ...).
- **Output Data**: It slices the data starting just after the input data for `output_chunk_length`, maintaining the same shifting method (T4 ~ T5 / T5 ~ T6 / ...).

- Let’s split the processed data into training and testing sets as an example.

```python
train, test = transformed[:-36], transformed[-36:]

plt.figure(figsize=(16, 3))
train.plot(label='train')
test.plot(label='test');
```

![png](/assets/img/2024-05-12-time-series-darts_files/2024-05-12-time-series-darts_19_0.png)

### Covariates

![covariates](https://unit8co.github.io/darts/_images/covariates-highlevel.png)

- When providing training data to the model, besides the target data, you can also supply relevant time series data as covariates. 
- These are referred to as `covariates` in Darts and can be classified into three main types:

1. **Past Covariates**: Represents historical values of time series that are known at the time of prediction. Generally, these are measurements or observations.
2. **Future Covariates**: Represents future values of time series known in advance during the prediction period. This could include known future holidays or weather forecasts.
3. **Static Covariates**: Values that remain constant over time (e.g., building type data for energy usage).

- Depending on the model, some may utilize only Past Covariates, some only Future Covariates, while others incorporate both. The choice of model will determine which covariates to provide. Due to the length of this post, we will focus only on Past and Future Covariates.

- Covariates can be created in two primary ways.

#### Creating Covariates External to the Model

- Before feeding data into the model, you can first generate covariates and then input them together with the target dataset.
- In this example, we will create past and future covariates from the month and year extracted from the dataset.

```python
from darts.utils.timeseries_generation import datetime_attribute_timeseries
from darts import concatenate

# Extract year and month data from transformed data
milk_year = datetime_attribute_timeseries(transformed, attribute='year')
milk_month = datetime_attribute_timeseries(transformed, attribute='month')

# Combine year and month data (stack)
milk_covariates = milk_year.stack(milk_month)

# Split covariates into train/test sets
milk_train_covariates, milk_val_covariates = milk_covariates[:-36], milk_covariates[-36:]

# Scale covariates using MinMaxScaler
scaler_covariates = Scaler()
milk_train_covariates = scaler_covariates.fit_transform(milk_train_covariates)
milk_val_covariates = scaler_covariates.transform(milk_val_covariates)

# Concatenate the train/test data and convert data type
milk_covariates = concatenate([milk_train_covariates, milk_val_covariates])
milk_covariates = milk_covariates.astype(np.float32)

plt.figure(figsize=(16, 3))
milk_covariates.plot();
```

![png](/assets/img/2024-05-12-time-series-darts_files/2024-05-12-time-series-darts_21_1.png)

- After setting up the covariates, you can specify them while fitting the model as follows:

```python
from darts.models import TiDEModel

model = TiDEModel(
    input_chunk_length=10,
    output_chunk_length=10,
)

model.fit(
    series=train,
    past_covariates=milk_covariates,
    future_covariates=milk_covariates,
)
```

#### Setting Covariates as Model Parameters
- In Darts, you can create covariates specifically for the model without declaring them explicitly.
- By adding the `add_encoders` parameter when creating the model, the selected covariates will automatically be included during training.

```python
add_encoders = {
    'cyclic': encoding data for datetime variables into sin/cos for past/future covariates.
    'datetime_attributes': raw datetime variables for past/future covariates.
    'custom': user-defined functions to create covariates.
    'transformer': functions to scale the additional covariate variables.
}
```

- The following code demonstrates how to utilize the `add_encoders` parameter during model declaration.

```python
from darts.models import TiDEModel

model = TiDEModel(
    input_chunk_length=12,
    output_chunk_length=12,
    n_epochs=100,
    random_state=0,
    use_reversible_instance_norm=True,
    add_encoders={
        'cyclic': {
            'past': ['month'] # Adds the "month" data as sin/cos encoded past covariates
            },
        'datetime_attribute': {
            'future': ['month', 'year'] # Adds "month/year" data as future covariates
            },
        'transformer': Scaler()
        }
)

model.fit(train)
```

- You can confirm that past and future covariates have been automatically added and scaled by accessing `model.past_covariates_series` and `model.future_covariates_series`.

```python
plt.figure(figsize=(16, 3))
model.past_covariate_series.plot();
```

![png](/assets/img/2024-05-12-time-series-darts_files/2024-05-12-time-series-darts_27_0.png)

```python
plt.figure(figsize=(16, 3))
model.future_covariate_series.plot();
```

![png](/assets/img/2024-05-12-time-series-darts_files/2024-05-12-time-series-darts_28_1.png)

## Making Predictions with the Trained Model
- Once the model has been trained, you can use the `predict()` function to make predictions.
- One of the basic parameters of predict, `n`, indicates how many steps ahead to forecast. If `n` is less than or equal to the model's `output_chunk_length`, the model will perform inference just once and trim the results to match the length of `n`.
- If `n` is greater than `output_chunk_length`, the model must be called repeatedly to predict `n`. Each call outputs `output_chunk_length` prediction points, proceeding recursively until the final `n` points are predicted. 

![more-ns](https://unit8co.github.io/darts/_images/prediction_multi.png)

```python
pred_less_n = model.predict(n=11)
pred_more_n = model.predict(n=24)
```

```python
plt.figure(figsize=(16, 3))
train.plot(label='train')
test.plot(label='test')
pred_more_n.plot(label='n > output_chunk_length', marker='8')
pred_less_n.plot(label='n < output_chunk_length', marker='.');
```

![png](/assets/img/2024-05-12-time-series-darts_files/2024-05-12-time-series-darts_31_0.png)

## Conclusion
- We explored how to preprocess time series data straightforwardly without complex coding and how to easily handle deep learning models with the Darts package.
- In the next post, we will explore how to establish a simple MLOps environment for managing experiments with time series deep learning models, using packages like Optuna and Hydra.