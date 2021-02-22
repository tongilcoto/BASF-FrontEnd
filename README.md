# BASF CHALLENGE. TEST 1&2. PYTHON with BEHAVE BDD framework
## TEST 1: Log In test
## TEST 2: Search test

## Pre-requisites

1. Python version 3 and pip
2. pipenv (pip install pipenv)

## Deployment

1. pipenv install --ignore-pipfile
2. pipenv shell

## Execution

1. export QKNOWS_USER={your username}
2. export QKNOWS_PASSWORD={your password}
3. behave --no-capture -f json -o reports/report.json

## Project lay out

Since it is a BDD project, it uses feature files for tests definition. The test plan is stored at "features/" folder, 
having each test a dedicated feature file

BDD needs a "glue" code, a decoder, in order to understand the feature files language. This code is stored at "steps/"
folder. This code performs the orchestrating of the test steps

There is also a "sut/" folder, which stores the code which controls the system under tests.

Under "sut/" folder there are two subfolders
- "model/": this one hosts the pages objects, which provides "gears" to perform actions
- "selectors/": this one hosts the selectors of the web elements in order to find them by the model. 
  They are kept separated in order to use them as configuration files, easier to maintain.

## TEST 1: Log In

It uses "features/As a QKnows user I want to successfully log in.feature.feature" as BDD feature file

## TEST 2: Search

It uses "features/As a QKnows user I want to check my search results.feature" as BDD feature file


## REPORT

Json report can be found at "reports/report.json"

## RESULTS

Both tests are passed, but the assertion library is using stricter matcher conditions than web search engine

For example, for "carbon" search, there is a result with "carbonate", which the library throws an error on

      Assertion Failed: 
      Expected: a string containing 'carbon'
           but: was 'The present invention relates to a process for the reduction of pitch in an aqueous medium generated in a papermaking or pulping process, comprising the following steps: a) providing an aqueous medium comprising pitch generated in a papermaking or pulping proc…'

In any case, it gives me the opportunity to try screenshots

## Exiting virtual env

1. exit