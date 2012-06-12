#!/bin/bash

echo "** Running Unit Tests **"


echo "** Photo Manager **"
coverage -e 
coverage -x manage.py test photo_manager --settings=settings.local


echo "** WRITING COVERAGE **"
coverage html -d ./reports/coverage_html
coverage -r -m >./reports/coverage_report.txt
