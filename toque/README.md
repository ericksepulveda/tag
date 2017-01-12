# csdpy
Template for Certified Scrum Developer course with Python

Install in a Debian/Ubuntu

    sudo apt-get update
    sudo apt-get install python-virtualenv
    sudo apt-get install libxml2-dev libxslt-dev python3-dev

    virtualenv -p python3 p3
    source p3/bin/activate


Installation

    git clone http://github.com/jgabardini/csdpy
    cd csdpy
    pip install -r requirements.txt

Test
- behave
- nosetests

Run
- python rover.py
- browse to localhost:5000
