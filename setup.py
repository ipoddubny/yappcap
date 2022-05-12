from setuptools import setup, find_packages
from Cython.Build import cythonize
import os

VERSION = '0.0.1'

if not os.path.exists('definitions.pxi'):
    os.system('make definitions.pxi')

    setup(
    name='yappcap',
    version=VERSION,  
    ext_modules=cythonize('yappcap.pyx'),
    install_requires=['wheel', 'setuptools', 'Cython'],
    packages=find_packages(),
    url='https://github.com/asterisk/yappcap',
)
