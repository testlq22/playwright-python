testpaths = tests  -  defines the folder containing test. If given the pytest will go directly
to this folder when searching for the tests to execute.

For Running a single test file use

pytest test_*.py
BUT!!!
It works only if you are in the folder containing test.
PS C:\webdriveriotest\pythonProject3\tests> pytest test_register.py    - working

PS C:\webdriveriotest\pythonProject3> pytest test_register.py   -DOESN'T work and error appears:
                                                                 ERROR: file or directory not found: test_register.py
