#!/usr/bin/env python
# coding: utf-8

# # Model Training
# 
# Cross-validation is a resampling procedure used to evaluate machine learning models on a limited data sample.
# 
# The procedure has a single parameter called k that refers to the number of groups that a given data sample is to be split into. As such, the procedure is often called k-fold cross-validation. In this tutorial, we split our training data into 5 groups, thus k=5 and our approach is refered to as 5-fold cross-validation.
# 
# In machine learning applications, we need to split out data into a training set (what is used to train the machine learning model) and a test set (a portion of data not used in training and reserved for evaluating how well the model is working). Cross-validation allows every data point to be used for both training and evaluation. It also helps us identify if any random splitting of the data results is drastically different performance.
# 
# The general procedure is as follows:
# 
# 1. Shuffle the dataset randomly.
# 2. Split the dataset into k groups
# 3. For each unique group:
#     Take one group as the test data set
#     Take the remaining groups as a training data set
#     Fit a model on the training set and evaluate it on the test set
#     Retain the evaluation score and discard the model
# 4. Summarize the skill of the model using the sample of model evaluation scores
# 
# Our tutorial notebook utilized 5-fold cross validation in all training examples.
# 
# We also provide examples of saving Machine Learning models as [Pickle files](https://scikit-learn.org/stable/model_persistence.html) as well as with the Joblib approach, which is often preferred as it offers model compression and smaller file sizes.
# 
# #### Feature Importance
# 
# <p>Feature importance is a technique for assessing how important each of our input features are to making accurate predictions. Features with low importance do not contribute much (are not used/do not have much weight) to prediction accuracy. Low importance features can be ignored creating simpler more scalable machine learning modesl.</p>
# 
# We use a technique called [Permutation Importance](https://scikit-learn.org/stable/modules/permutation_importance.html) in which features are randomly shuffled. If a column's values can be randomly shuffled and prediction accuracy does not decrease, then that feature has low importance.
# 
# Examples of permutation importance and the retraining of models using fewer features is provided.
# 

# In[ ]:




