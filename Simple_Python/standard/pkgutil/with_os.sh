#! /bin/sh
export PYTHONPATH=os_${1}
echo "PYTHONPATH=$PYTHONPATH"
echo

python2 pkgutil_3.py