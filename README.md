# Setup instructions

## Install Python
brew install python

## Install PIP
```
curl -O http://python-distribute.org/distribute_setup.py
python distribute_setup.py
curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
python get-pip.py
```
## Install Flask
```
pip install --upgrade pip
pip install flask
```
# command to start the application
python app.py

# Turn on debug mode
python app.py True

# command to run the unit tests for your application
## Accept header not set to application/json
curl --header "Accept: xxx" http://127.0.0.1:5000/

## Accept header set to application/json
curl --header "Accept: application/json" http://127.0.0.1:5000/

## no Accept header
curl -H 'Accept:' http://127.0.0.1:5000/

## POST request
curl -X POST http://127.0.0.1:5000/

## run unit test
python test.py

