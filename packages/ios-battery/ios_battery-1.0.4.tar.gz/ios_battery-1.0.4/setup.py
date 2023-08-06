from distutils.core import setup
from setuptools import find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(name='ios_battery',
      version='1.0.4',
      description='get ios battery',
      long_description=long_description,
      author='cfr',
      author_email='1354592998@qq.com',
      install_requires=[],
      license='MIT',
      packages=find_packages(),
      platforms=['all'],
      classifiers=[],

      entry_points={
          'console_scripts':['ios_battey=ios_battery.battery:main']
      },



      )
