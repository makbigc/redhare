from setuptools import setup

setup(name='redhare',
      version='0.1',
      author='Mak Sze Chun',
      entry_points={
          'console_scripts': ['redhare=cli:cli'],
          }
      )
