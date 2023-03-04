#!/usr/bin/env python
# coding: utf-8

# # Model Development and Paramter Tuning
# 
# #### Use Case Driven Model Development
# 
# The type of classification model needed depends on the application. For example, during a flood emergency, first responders may only be interested in identifying residential buildings. In this use case, binary classification (Residential vs. non-Residential) is sufficient. 
# 
# However, for ecomomic applications, multiclass classification is needed, i.e. Residential vs. Commercial vs. Industrial vs. ...
# 
# We provide examples of both scenarios.
# 
# #### Binary Classification
# 
# First, we need to preprocess the data and prepare it for machine learning. For this binary classification example, all non-Residential building types are changed to "Other".
# 
# <p>The OsmNearestRoad and OrnlType are currently text. We need to encode these as integers before proceeding with machine learning. We also want to scale our columns to a common axis so that columns with large values don't bias the learning.</p>
# 
# <p>We'll use a standard scaler, which scales based on the standard scoreas: z = (x - u) / s</p>
# <p>Where u is the mean of the training samples and s is the standard deviation of the training samples</p>
# 
# <p>Binary classification is demonstrate in the tutorial notebook via two methods: Random Forest and Neural Network.</p>
# 
# #### Binary Classification - Strategies to deal with imbalanced classes
# 
# ##### Undersampling
# 
# <p>As discussed in Chapter 2, our data is heavily imbalanced. The tutorial notebook presents two strategies for dealing with this imbalance.</p>
# 
# Undersampling refers to a group of techniques designed to balance the class distribution. Undersampling techniques remove examples from the training dataset that belong to the majority class in order to better balance the class distribution. 
# 
# This is in contrast to oversampling, which involves adding examples to the minority class in an effort to reduce the class distribution imbalance.
# 
# Near Miss refers to a collection of undersampling methods that select examples based on the distance of majority class examples to minority class examples.
# 
# The approaches were proposed by Jianping Zhang and Inderjeet Mani in their 2003 paper [KNN Approach to Unbalanced Data Distributions: A Case Study Involving Information Extraction](https://www.site.uottawa.ca/~nat/Workshop2003/jzhang.pdf)
# 
# There are three versions of the technique, named NearMiss-1, NearMiss-2, and NearMiss-3.
# 
# * NearMiss-1 selects examples from the majority class that have the smallest average distance to the k closest examples from the minority class. 
# * NearMiss-2 selects examples from the majority class that have the smallest average distance to the k furthest examples from the minority class. 
# * NearMiss-3 involves selecting a given number of majority class examples for each example in the minority class that are closest.
# 
# Distance is determined in feature space using Euclidean distance.
# 
# We use NearMiss-3, which keeps majority class examples that are on the decision boundary.
# 
# ##### Threshold moving
# 
# Perhaps the simplest approach to handle a severe class imbalance is to change the decision threshold. Many classification algorithms will return a probability of class membership where all values equal or greater than a threshold are mapped to one class and all other values are mapped to the other class. The default of many algorithms is to set the threshold at 0.5. Threshold moving simply moves the threshold attempting to achieve higher accuracy.
# 
# #### Multiclass Classification
# 
# What does all of this look like if we want to do multiclass classification instead of binary classification? The tutorial notebook looks at another use case where we want to classify a building as "Residential", "Commercial", or "Industrial".
# 
# #### Multiclass Classificiation - Strategies for dealing with imbalanced classes
# 
# ##### One-vs-One Classification 
# 
# One-vs-One classification is a multi-class classification strategy for dealing with unbalanced classes. The One-vs-One strategy splits a multi-class classification into one binary classification problem per each pair of classes, e.g. Residentail vs. Commercial, Residential vs. Industrial, Commercial vs. Industrial. The final class assignment is determined by aggregating the results of the binary classifiers.
# 
# ##### One-vs-Rest Classification
# 
# The One-vs-Rest strategy is a related approach for dealing with multiclass imbalance. Here, fewer models are created. There is one binary classification problem per class, e.g. Residentail vs. Rest, Commercial vs. Rest, Industrial vs. Rest.
# 
# The tutorial notebook, Building_Classification.ipynb, provides examples of both strategies as well as examples of dealing with class imbalance in neural networks.

# In[ ]:




