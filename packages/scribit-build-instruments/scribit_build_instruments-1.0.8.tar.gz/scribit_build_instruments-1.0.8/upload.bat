py -m build
py -m twine upload --repository pypi dist/*
pip uninstall scribit_build_instruments -y
pip install scribit_build_instruments
pip uninstall scribit_build_instruments -y
pip install scribit_build_instruments