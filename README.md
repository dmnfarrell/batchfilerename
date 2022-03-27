# batch file rename

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

<img align="right" src=img/logo.png width=150px>

This is a simple batch file renaming utility written in Python. You can install with:

`pip install batchfilename`

Install from github:

pip install -e git+https://github.com/dmnfarrell/batchfilename.git#egg=batchfilename

## How to use

Run using the command `batchfilename`. A window with two panes will appear. Select the folder where the files are to be renamed. On the left the files will be listed, onthe right a preview of the renamed files is shown. You can then select the symbols to find and replace with, which will be applied to all files. Filter the files if needed, '*.*' means all files. Always use 'preview' first to check the results before executing as some file name changes might not be reversible. The 'occurences' option allows you to only replace a specific number of instances of a symbol in the name.

## Screen shot

<img src=img/scr1.png width=500px>

## TO DO

* add undo option
* multiple/recursive folders
* manually remove items
