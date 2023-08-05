from setuptools import setup, find_packages

"""
# Commands
- change to directory
python setup.py sdist
python -m twine upload  dist/* -u friebertshaeusertraideai -p DJQ3yjk4ark_ynu!una
# Result
https://pypi.org/project/pf-test-hello-world/0.0.1/
"""



REQUIREMENTS = ['numpy', 
                'pandas']

setup(
  name='helper_utils',
  version='0.0.5',
  description='Helper functions',
  long_description="Helper functions",
  url='',  
  author='Philipp Friebertshäuser',
  author_email='friebertshaeuser@traide.ai',
  license='MIT', 
  keywords='helper', 
  packages = find_packages(),
  install_requires=REQUIREMENTS
)