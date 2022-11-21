#!/bin/bash 

# run from project root directory as ./codetools/coverage.sh
COVERAGE_RCFILE=./codetools/.coveragerc coverage run -m unittest discover ./tests/

coverage report -m

