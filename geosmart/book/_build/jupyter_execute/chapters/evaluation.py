#!/usr/bin/env python
# coding: utf-8

# # Performance Evaluation
# 
# We are using balanced accuracy to deal with our imbalanced dataset. It is defined as the average of recall obtained on each class. Similarly, we use micro F1, which is the normal F1 formula but calculated using the total number of True Positives (TP), False Positives (FP) and False Negatives (FN), instead of individually for each class.
# 
# Results are also presented as a confustion matrix, which is a visual display of true positives, true negatives, false positives, and false negatives.
# 
# See Building_Classification.ipynb for step-by-step evaluation that leads to 
# 
# <p>
# <center>Binary Classification</center>
# 
# | Approach | Accuracy | Micro F1 
# -----------|----------|----------
# | Random Forest | 85.5% | 0.962 
# | Random Forest w/ balanced classes | 84% | 0.84
# | Random Forest w/ threshold moving | 86.7% | 0.963
# | Neural Network w/ class weighting | 87.4% | 0.894
# </p>
# 
# <br/>
# 
# <p>
# <center>Multiclass Classification</center>
# 
# | Approach | Accuracy | Micro F1 
# -----------|----------|----------
# | Random Forest | 70% | 0.96 
# | Random Forest w/ one-vs-one | 70% | 0.96
# | Random Forest w/ one-vs-rest | 67% | 0.963
# | Neural Network w/ class weighting | 33% | 0.92
#  </p>

# In[ ]:




