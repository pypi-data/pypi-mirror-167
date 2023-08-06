del /S /Q  dist\*.gz
python setup.py sdist && twine upload dist/*

pause