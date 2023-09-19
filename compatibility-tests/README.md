### Goal

The aim of this repo was to test all python versions from 3.7.0 to 3.9.6 for compatibility with the codebase.

### Files

1. run.sh

 A) Downloads all python versions and extracts the contents
 B) Opens a subshell and installs python
 C) Installs all the dependencies used by the Injective Exchange API and Chain Client
 D) Saves the python version and the stdout/stderr of the tests.py script to the results.txt file to have both successful and error output.
 E) Purges python and all its dependencies, repeats until the last version.

- NOTE: DO NOT USE THIS SCRIPT IN YOUR OWN MACHINE, USE IT ONLY IN A TEST ENVIRONMENT AS THE SCRIPT WILL UNINSTALL ALL THE DEPENDENCIES THAT COME WITH PYTHON.

 2. tests.py

This python script imports all the libraries used by the Injective Exchange API and Chain Client. It makes a gRPC request and uses the data to broadcast a transaction to the chain with both cosmos-sdk and exchange messages using a REST API endpoint. Certain libraries are imported from injective-py which you can find [here](https://pypi.org/project/injective-py/).

 3. results.txt

This file contains the python version for each run and the output of tests.py

### Results

Evidently, all the libraries are compatible with python 3.7.0 up to 3.9.6 as per the results.txt file

`Modifications for compatibility in Python 3.7`

Python 3.7 requires one small modification in the file typings.py to be compatible with the codebase.

- File: chain_client/_typings.py
- Current code: from typing import Literal, TypedDict
- Change to: from typing_extensions import Literal, TypedDict

API users must also install the typing_extensions library with the below command.

```bash
pip3 install typing_extensions
```

The Python 3.7 stdlib has an older version of typing.py so the above change in the code will fix the compatibility issue by importing Literal from typing_extensions
