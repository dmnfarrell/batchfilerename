from setuptools import setup
import sys,os

setup(
    name = 'batchfilerename',
    version = '1.0',
    description = 'Batch file renaming utility',
    long_description = ' Batch file rename is a simple tool to rename multiple files at once by find/replace',
    url='https://github.com/dmnfarrell/batchfilerename',
    license='GPL v3',
    author = 'Damien Farrell',
    author_email = 'farrell.damien@gmail.com',
    py_modules = ['rename'],
    install_requires=[],
    entry_points = { 'gui_scripts': [
                     'batchfilerename = rename:main']},
    classifiers = ['Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX',
            'Topic :: Software Development :: User Interfaces',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Development Status :: 4 - Beta',
            'Intended Audience :: Science/Research'],
    keywords = ['tkinter', 'file management', 'tools'],
)
