#!/bin/bash
echo -n "Removing *.pyc ------------------------------------------ "
find . -type f -name "*.pyc" -exec rm -rf "{}" \;
echo "Done"
echo -n "Initing server ------------------------------------------ "
python manage.py runserver 8000 &> /dev/null  &
echo "Done"
coverage erase
echo "API Tests"
coverage run --source='api' manage.py test api
coverage report -m
coverage html -d ../coverage/API
echo ""
echo "APP Tests"
coverage run --source='app' manage.py test app
coverage report -m
coverage html -d ../coverage/APP
echo -n "Killing everything -------------------------------------- "
killall -9 coverage python test_coverage.sh -q
echo "Killed"
