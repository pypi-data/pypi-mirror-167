# Python Packages

1. create `setup.py` file.
2. build all the necessary packages that Python will require and create source distribution 
```bash
# install
pip install wheel

# create dist, build
python setup.py sdist bdist_wheel
```
3. Deploy to PyPi
```bash
# install
pip install twine

# deploy package
twine upload dist/*
```

### Sources 
[Guide](https://www.freecodecamp.org/news/build-your-first-python-package/)