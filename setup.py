from Cython.Build import cythonize
from setuptools import setup, find_packages
import os

VERSION = '0.0.1'

if not os.path.exists('definitions.pxi'):
    os.system('make definitions.pxi')

setup(
    name='yappcap',
    version=VERSION,  
    ext_modules=cythonize('yappcap.pyx'),
    packages=find_packages(),
    url='https://github.com/asterisk/yappcap'
)
