#!/bin/bash
echo -n "Removing *.pyc ------------------------------------------ "
find . -type f -name "*.pyc" -exec rm -rf "{}" \;
echo "Done"
coverage erase
echo "API Tests"
coverage run --source='api' manage.py test api
coverage report -m
coverage html -d ../coverage/API
echo -n "Killing everything -------------------------------------- "
killall -9 coverage python test_coverage.sh -q
echo "Killed"
