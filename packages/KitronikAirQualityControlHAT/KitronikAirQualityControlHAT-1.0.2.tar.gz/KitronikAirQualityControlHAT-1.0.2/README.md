# air-quality-control-board
## Setup needed:
- pip install -U pip wheel setuptools
- pip install --no-cache-dir --force-reinstall --only-binary=cryptography cryptography
- pip install -U twine
- sudo pip install rpi_ws281x
- python setup.py sdist bdist_wheel
- python -m twine check dist/*
- python -m twine upload -r testpypi dist/*
- pip install -i https://test.pypi.org/simple KitronikAirQualityControlHAT
- python -m twine upload dist/*
- sudo pip install -i https://pypi.org/simple KitronikAirQualityControlHAT
- sudo python test_all.py
