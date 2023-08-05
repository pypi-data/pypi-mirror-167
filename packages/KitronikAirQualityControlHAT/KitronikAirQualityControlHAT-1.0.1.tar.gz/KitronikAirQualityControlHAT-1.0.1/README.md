# air-quality-control-board
## Setup needed:
- pip install -U pip wheel setuptools rpi_ws281x
- pip install --no-cache-dir --force-reinstall --only-binary=cryptography cryptography
- pip install -U twine
- python setup.py sdist bdist_wheel
- python -m twine check dist/*
- python -m twine upload -r testpypi dist/*
- pip install -U -i https://test.pypi.org/simple/ KitronikAirQualityControlHAT
- python -m twine upload dist/*
- pip install KitronikAirQualityControlHAT
