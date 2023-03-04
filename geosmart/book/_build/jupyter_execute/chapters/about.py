#!/usr/bin/env python
# coding: utf-8

# # About the GeoSMART Use Case Library
# 
# ### General Overview
# 
# Explain this family of books, link to others, explain how to contribute and purpose. Books in the library can be identified by the badge:
# 
# [![GeoSMART Use Case](../img/use_case_badge.svg)](https://geo-smart.github.io/usecases)
# 
# ### Contributing Content
# 
# Tutorial content can be integrated into jupyterbooks in one of two ways:
# * Do it yourself (use this template book and add your content)
# * Provide use your content (preferably in a github repo) and we will integrate it
# 
# The goal is to provide executable code on some platform. The contributor can choose between:
# * Binder
# * Google Colab
# * Free AWS (smaller cloud-based examples)
# If none of the above options work for you, please contact us directly to discuss further.
# 
# ### Technical Details
# 
# Creating a use case book can either be done by navigating use case template repository and clicking the "use as template" button.
# 
# The `.github` folder already contains the github actions that will handle CI/CD deployment to github pages. There is no need to create a gh-pages branch, the first run of the github actions should handle that automatically.
