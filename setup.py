from setuptools import setup
import sys,os

with open('description.txt') as f:
    long_description = f.read()

setup(
    name = 'batchfilerename',
    version = '1.0',
    description = 'Batch file renaming utility',
    long_description = long_description,
    url='https://github.com/dmnfarrell/batchfilerename',
    license='GPL v3',
    author = 'Damien Farrell',
    author_email = 'farrell.damien@gmail.com',
    packages = ['batchfilerename'],
    package_data={'batchfilerename': ['img/logo.gif',
                                      '../description.txt',]},
    install_requires=[],
    entry_points = { 'gui_scripts': [
                     'batchfilerename = batchfilerename.rename:main']},
    classifiers = ['Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX',
            'Topic :: Utilities',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Development Status :: 4 - Beta'],
    keywords = ['tkinter', 'file management', 'tools'],
)
