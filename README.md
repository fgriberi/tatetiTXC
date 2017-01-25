# csdpy
Template for Certified Scrum Developer course with Python

#Install
##Install in a Debian/Ubuntu

Puede usarse como base el csd-box https://github.com/kleer-la/virtual-machines

    sudo apt-get update
    sudo apt-get install python-virtualenv
    sudo apt-get install libxml2-dev libxslt-dev python3-dev

    virtualenv -p python3 p3
    source p3/bin/activate

##App template

    git clone http://github.com/jgabardini/csdpy
    cd csdpy
    pip install -r requirements.txt

##Optional
- Tab-complete for python http://blog.e-shell.org/221

#Test
- behave
- nosetests

#Run
- python rover.py
- browse to localhost:5000
