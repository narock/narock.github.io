#!/usr/bin/env python
# coding: utf-8

# # Data Preparation
# 
# Our goal is to predict a building's type (Residential/Commercial/Industrial) based on known features of the building (area, location, etc.). To accomplish this, we gather as many building features as possible from open datasets. We begin with as large a set as possible and will work towards identifying each feature's actual importance. 
# 
# Our sources of building features are [Open Street Map (OSM)](https://www.openstreetmap.org), the [Multi-Resolution Land Characteristics Consortium (MRLC)](https://www.mrlc.gov/data/type/urban-imperviousness), [United States Census' County Business Patterns (CBP)](https://www.census.gov/programs-surveys/cbp/data/tables.html), and the [United States Census' American Community Survey (ACS)](https://www.census.gov/programs-surveys/acs/data.html).
# 
# We've preprocessed the data to spatially align all the features. For example, we used building longitude and latitude provided by OSM to determine which county the building resides in. We've then gone to the ACS and looked up socio-econimic data such as median income and housing density. The resulting machine learning ready data looks like this:
# 
# | Column      | Description | Source |
# | :---------: | :---------- |:-------|
# | X                    | X coordinate of the building in the EPGS:5070 system  | OSM |
# | Y                    | Y coordinate of the building in the EPGS:5070 system  | OSM |
# | Area                 | Area of building in square meters        | OSM |
# | MedianIncomeCounty   | Median income of the county in which the building resides        | ACS |
# | HousingUnitsCounty   | Number of housing units in the county in which the building resides | ACS |
# | HousingDensityCounty | Number of housing units in the county divided by the number of people residing in the county where the building resides        | ACS |
# | Impervious           | Percentage of the area surrounding the building that is comprised of impervious surfaces such as roads and other paved surfaces. Value provided is the mean area weighted average of imperviousness underneath the building footprint  | MRLC |
# | AgCount              | Number of agricultural businesses in the county in which the building resides | CBP |
# | CmCount              | Number of commercial businesses in the county in which the building resides   | CBP |
# | GvCount              | Number of government buildings in the county in which the building resides    | CBP |
# | EdCount              | Number of educational buildings in the county in which the building resides   | CBP |
# | InCount              | Number of industrial buildings in the county in which the building resides    | CBP |
# | OsmNearestRoad       | Type of nearest road to the building | OSM |
# | BuildingType             | Building classification | FEMA |
# 
# The last column, 'BuildingType', is what we are trying to predict. [USA Structures](https://gis-fema.hub.arcgis.com/pages/usa-structures) is an open source building inventory provided by the Department of Homeland Security, FEMA, Oak Ridge National Laboratory, and the U.S. Geological Survey. The building inventory contains a Building Occupany Type, which was determined through census and U.S. mail data. Currently, Building Occupancy Type values are availble for nine states. However, we note that not every building in those nine states has a manually identified occupany type. We are using North Carolina Building Occupany Type data as our "ground-truth". If we can predict known building types well, the machine learning models can be reliably deployed on unknown buildings and in states where Building Occupany Type is unavailable.
# 
# The raw data used to create our machine learning ready data was too large to include on GitHub with this tutorial. If you are interested in the raw data see [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7696864.svg)](https://doi.org/10.5281/zenodo.7696864) and look in the "preprocessing" folder for our preprocessing code.
# 
