#!/bin/bash
python3.8 -m venv layers
source layers/bin/activate
pip3.8 install -r Requirements.txt  -t ./Layers
deactivate
zip -r Layers.zip ./Layers/