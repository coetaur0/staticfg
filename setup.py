from setuptools import setup


setup(name='staticfg',
      version=0.1,
      description='Control flow graph generator for Python3 programs',
      author='Aurelien Coet',
      author_email='aurelien.coet19@gmail.com',
      packages=['staticfg'],
      install_requires=[
        'astor',
        'graphviz',
      ])
