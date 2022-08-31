from setuptools import setup, find_packages

setup(
    name='CubeChess',
    version='0.1.0',
    packages=find_packages(include=['CubeChess', 'CubeChess.pieces'])
)