#!/usr/bin/env python
# coding: utf-8

# # Machine Learning Methods and Tools
# 
# The type of classification model needed depends on the application. For example, during a flood emergency, first responders may only be interested in identifying residential buildings. In this use case, binary classification (Residential vs. non-Residential) is sufficient.
# 
# However, for ecomomic applications, multiclass classification is needed, i.e. Residential vs. Commercial vs. Industrial vs. ...
# 
# We provide examples for both scenarios.
# 
# Our data is heavily unbalanced. The number of buildings by type is:
# 
# | Building Type | Count |
# ----------------------|-------------
# |Residential |        976690 |
# |Commercial  |        64029 |
# |Industrial  |         16722 |
# |Assembly    |         7323 |
# |Education    |         6457 |
# |Government    |        4910 |
# |Agriculture    |       1651 |
# |Utility and Misc  |      362 |
# 
# We also provide examples of how to deal with unbalanced classes in both binary classification and multi-class classification.
# 
