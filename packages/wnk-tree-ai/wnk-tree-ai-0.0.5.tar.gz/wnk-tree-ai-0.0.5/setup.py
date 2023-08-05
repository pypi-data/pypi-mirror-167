from setuptools import setup, find_packages

"""
# Commands
python setup.py sdist
python -m twine upload  dist/* -u friebertshaeusertraideai -p DJQ3yjk4ark_ynu!una
# Result
https://pypi.org/project/pf-test-hello-world/0.0.1/
"""

# this grabs the requirements from requirements.txt

with open("./requirements.txt") as f:
    REQUIREMENTS = [i.strip() for i in f.readlines()]


setup(
  name='wnk-tree-ai',
  version='0.0.5',
  description='Nomenclature for AI Traversal',
  long_description="Nomenclature for AI Traversal",
  url='',  
  author='Philipp Friebertshäuser',
  author_email='friebertshaeuser@traide.ai',
  license='MIT', 
  keywords='wnk', 
  packages = find_packages(),
  install_requires=REQUIREMENTS
)