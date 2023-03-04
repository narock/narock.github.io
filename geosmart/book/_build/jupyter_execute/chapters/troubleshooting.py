#!/usr/bin/env python
# coding: utf-8

# # Trouble Shooting
# 
# This page lists all the issues we have met when creating or following tutorials.
# 
# If you have no issues with running the tutorials, you can skip this chapter. It is very likely that some platform specific issues happen now and then, we would love to collect those knowledge to help students in future to avoid wasting time on them. 
# 
# In this chapter, each section should address one techincal issue/concern. Please list your running environment in many details as possible. The following is an example:

# ### Example Issue: Cannot run the `model.train` in Chapter 2. It omits error: "xxxxx".
# 
# #### Environment
# Machine: Apple M1 laptop
# Python: 3.10
# Conda: 4.12
# Scikit-learn: 1.0.2
# ...
# 
# #### Code
# Line 1xxx in Chapter 2 (link)
# ```
# clf = RandomForestClassifier(max_depth=2, random_state=0)
# clf.train(X, y)
# ```
# 
# #### Error
# raised Error xxxx
# 
# #### Diagnose
# This might be caused by the incompatibility among xxxx
# 
# #### Solution
# Please remove xxx, install xxx, and do xxx to try again. 
