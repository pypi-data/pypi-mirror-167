from setuptools import setup, find_packages

"""
# Commands
python setup.py sdist
python -m twine upload  dist/* -u friebertshaeusertraideai -p DJQ3yjk4ark_ynu!una
# Result
https://pypi.org/project/pf-test-hello-world/0.0.1/
"""

setup(
  name='wnk-tree-ai',
  version='0.0.2',
  description='Nomenclature for AI Traversal',
  long_description="Nomenclature for AI Traversal",
  url='',  
  author='Philipp Friebertshäuser',
  author_email='friebertshaeuser@traide.ai',
  license='MIT', 
  keywords='wnk', 
  packages = find_packages(),
  install_requires=[''] 
)