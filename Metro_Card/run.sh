#!/bin/bash
pip3 install -r requirements.txt
coverage run -m unittest discover
coverage report
python3 -m geektrust sample_input/input1.txt