# Run Tests
python3 -m unittest

# Run Coverage
coverge run -m unittest

# check report
coverage report

# check html coverage
coverage html

# zip folder
zip -r <ZIP_FILENAME> <FOLDER_LOCATION>

# Remove all pycache files
find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf