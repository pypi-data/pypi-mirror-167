from setuptools import setup, find_packages

"""
# Commands
python setup.py sdist
python -m twine upload  dist/* -u friebertshaeusertraideai -p DJQ3yjk4ark_ynu!una
# Result
https://pypi.org/project/pf-test-hello-world/0.0.1/
"""

# this grabs the requirements from requirements.txt



REQUIREMENTS = ['treelib==1.6.1', 
                'numpy==1.22.4', 
                'pandas==1.4.2',
                'pydantic==1.9.0']

setup(
  name='wnk-tree-ai',
  version='0.0.7',
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