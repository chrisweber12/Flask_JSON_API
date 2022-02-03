!#/bin/sh
export FLASK_APP=__init__.py
source venv/bin/activate
flask run -h localhost -p 3000
