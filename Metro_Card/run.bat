@echo off
pip install -r requirements.txt
coverage run -m unittest discover
coverage report
py -m geektrust sample_input\input1.txt