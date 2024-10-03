#!/bin/bash
# which pip && pip install virtualenv
# which pip3 && pip3 install virtualenv

python3 -m venv learning-env
source env/bin/activate
pip install -r requirements.txt
