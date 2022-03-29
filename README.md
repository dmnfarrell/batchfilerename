# batch file rename

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

<img align="right" src=batchfilerename/img/logo.png width=150px>

This is a simple batch file renaming utility written in pure Python. You can install with:

`pip install batchfilename`

Install from github:

```pip install -e git+https://github.com/dmnfarrell/batchfilename.git#egg=batchfilename```

## How to use

Run using the command `batchfilename`. A window with two panes will appear. Select the folder where the files are to be renamed. On the left the files will be listed and on the right a preview of the renamed files is shown (without full path for ease of viewing). You can then select the symbols to find and replace with, which will be applied to all files. Filter the files to be renamed if needed, `*.*` means all files. **Always use 'preview'** first to check the results before executing as some file name changes might not be reversible. Though you should be able to reverse the last run using the undo button.

### Other features

* The 'occurences' option allows you to only replace a specific number of instances of a symbol in the name.
* Undo the previous renaming step (assuming you have not quit the program)
* Recursively load a folder

## Screenshot

<img src=batchfilerename/img/scr1.png width=500px>

## TO DO

* manually remove items from file list
