#!/bin/bash
python3.8 -m venv pandas
source pandas/bin/activate
pip3.8 install pandas fitparse  -t ./Layer
deactivate
zip -r Layer.zip ./Layer/