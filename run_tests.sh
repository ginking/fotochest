#!/bin/bash

echo "** Running Unit Tests **"


echo "** Photo Manager **"
coverage -e 
coverage -x manage.py test photo_manager --settings=settings.local

echo "** Running PyFlakes **"

cd apps
pyflakes photo_manager
pyflakes administrator

echo "** Running Pep8 **"
pep8 photo_manager  --exclude=migrations --show-pep8
pep8 administrator --exclude=migrations --show-pep8

cd ..

echo "** WRITING COVERAGE **"
coverage html -d ./reports/coverage_html
coverage -r -m >./reports/coverage_report.txt
