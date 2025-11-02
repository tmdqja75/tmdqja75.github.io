---
layout: post
title: Introduction to Time Series Data
description: >
  An insightful exploration into the fundamentals of time series analysis and its significance across various fields.

image: /assets/post_banner/time-series.jpeg
categories: mldl
sitemap:
    changefreq : weekly
comments: true
---

* this list will be replaced by the table of contents
{:toc}

# Time Series Data

Time series analysis is utilized across a multitude of fields. Analyzing user access logs or behaviors can also be approached through the lens of time series analysis. This type of analysis encompasses basic statistical models such as ARIMA, as well as deep learning-based models like RNN and CNN+LSTM. Although deep learning is considered cutting-edge technology, the importance of traditional statistical models should not be overlooked. Generally, when there are no outliers present, traditional models like ARIMA may perform better. In other words, when the data exhibits clear patterns, machine learning techniques tend to excel, while deep learning techniques often shine with more complex patterns.

What issues may arise when we introduce the attribute of time? The mean and variance intrinsic to general data can change due to the temporal attribute, making pattern recognition more challenging. Existing models typically assume a normal distribution for their analyses, which can lead to errors when time series data is fed into these models. This is because traditional models assume stationarity.

# Properties of Time Series Data

Typically, time series data consists of three components: Trend Component, Seasonal Component, and Residuals or Irregular Component. The trend component indicates the prevailing direction in which the graph moves. The seasonal component refers to patterns that repeat over time, while the residual component signifies the parts of the data that remain unexplained after removing the trend and seasonal components. Thus, the assumption is that time series data is generated through these components.

# Stationarity and Non-Stationarity

So, what do the terms stationarity and non-stationarity mean? A stationary time series has a consistent mean and variance, irrespective of the passage of time, while a non-stationary time series features fluctuating mean and variance over time. It is significantly challenging to transform a non-stationary time series into a stationary one when working with actual data. Therefore, stationarity is categorized into two types: strict stationarity and weak stationarity. Strict stationarity is almost non-existent, while weak stationarity refers to a scenario where the mean remains constant regardless of time, yet the variance changes with lags.

# Auto-Correlation

Auto-correlation means examining the correlation coefficients among a time series’s own data points. It assesses the relationships between intervals in the time series. How do we compute auto-correlation? The key is by introducing time lags. By applying lags of 1, 2, 3, etc., to the data and calculating the correlation with lag 0, we can compute the auto-correlation based on changes in the lags.

This leads us to create the Auto-Correlation Function (ACF), which indicates the degree of association between observations at varying lags. For stationary time series, ACF rapidly decreases to zero. In the case of weak stationarity, since the variance shifts with lag, ACF will also decline quickly. Conversely, a non-stationary time series typically sees ACF decreasing slowly and often exhibiting substantial values. If the ACF becomes chaotic, it is an indicator of a non-stationary time series.