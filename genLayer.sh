#!/bin/bash
python3.7 -m venv pandas
source pandas/bin/activate
pip install pandas fitparse  -t ./python
deactivate
zip -r python.zip ./python/