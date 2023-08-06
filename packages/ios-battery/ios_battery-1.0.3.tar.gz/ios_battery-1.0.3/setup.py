from distutils.core import setup
from setuptools import find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(name='ios_battery',
      version='1.0.3',
      description='get ios battery',
      long_description=long_description,
      author='cfr',
      author_email='1354592998@qq.com',
      install_requires=['tidevice'],
      license='BSD License',
      packages=find_packages(),
      platforms=['all'],
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],

      entry_points={
          'console_scripts':['ios_battey=ios_battery.get_tidevice_battery:main']
      },



      )
