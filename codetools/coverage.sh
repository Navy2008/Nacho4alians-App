#!/bin/bash 

# run from project root directory as ./codetools/coverage.sh
# or specify --rcfile=path/filename as an argument when running manually
echo "[*] [$0]: **** Running tests with coverage ****"
echo ""
COVERAGE_RCFILE=./codetools/.coveragerc coverage run -m unittest discover ./tests/

echo "[*] [$0]"
echo "**** Generate HTML Coverage Report **** "
COVERAGE_RCFILE=./codetools/.coveragerc coverage html
echo "report index: file://$(pwd)/coverage_html_report/index.html"

echo "[*] [$0]"
echo "**** Coverage Report **** "
COVERAGE_RCFILE=./codetools/.coveragerc coverage report -m

