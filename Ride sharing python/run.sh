#!/bin/bash

pip install -r requirements.txt
coverage run -m unittest discover
coverage report
python -m geektrust sample_input/input1.txt