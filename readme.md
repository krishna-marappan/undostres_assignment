# To run or review this script please follow below procedure

To start with automation

# Pre-requisite

1. Install Python v3.x
2. Install Git

# Create Virtual environment

From cmd prompt CD to Project directory location

## On Windows

python -m pip install --upgrade pip
pip install -r dependencies/requirements.txt

##On Linux/Mac

pip3 install -r tests\dependencies/requirements.txt

## To Execute please use any one of the cmd

1. behave -f allure_behave.formatter:AllureFormatter -o Output feature
2. behave -f html -o Output/report.html
3. behave

## Overview of the project and folders

  This script is automated using "selenium" with "BDD framework" by "Python" language
  
Folders:
1. Data = It is used for the Xpath, Url, Data 
2. features =  It has one feature file written in the Gherkin programming language and
              one step file which is written in the Python language and this folder is
              the core project folder.
3. feature_support = It is mainly used for support file for features files which is written in 
                      python language major code will be available here
4. output =  It is only suitable for screenshots and reports.
5. dependencies =  Used to describe the requirements for this script.

## To view report 
 To use allure report run the below cmd in terminal
       " allure serve Output "
 To use behave-html report check in outputfolder