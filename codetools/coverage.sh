#!/bin/bash 

# run from project root directory as ./codetools/coverage.sh
echo "[*] [$0]: **** Running tests with coverage ****"
echo ""
COVERAGE_RCFILE=./codetools/.coveragerc coverage run -m unittest discover ./tests/

echo "[*] [$0]"
echo "**** Coverage Report **** "
coverage report -m

