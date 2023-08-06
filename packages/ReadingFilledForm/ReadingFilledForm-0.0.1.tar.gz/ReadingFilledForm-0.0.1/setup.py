##############################################
#### Written By: SATYAKI DE               ####
#### Written On: 20-Dec-2019              ####
#### Modified On 20-Dec-2019              ####
####                                      ####
#### Objective: Main scripts for logging  ####
##############################################

from setuptools import setup, find_packages

setup(
name="ReadingFilledForm",
version="0.0.1",
author="Satyaki De",
description="This is the main calling python script that will invoke the class to initiate the reading capability & display text from a formatted forms.",
packages=find_packages(exclude=['Scans','Template'])
)
