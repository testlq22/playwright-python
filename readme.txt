testpaths = tests  -  defines the folder containing test. If given the pytest will go directly
to this folder when searching for the tests to execute.

For Running a single test file use

pytest test_*.py
BUT!!!
It works only if you are in the folder containing test or manually specify folder name .
PS C:\webdriveriotest\pythonProject3\tests> pytest test_register.py    - working

PS C:\webdriveriotest\pythonProject3\pytest tests/test_register.py    - working

PS C:\webdriveriotest\pythonProject3> pytest test_register.py   -DOESN'T work and error appears:
                                                                 ERROR: file or directory not found: test_register.py

PS C:\webdriveriotest\pythonProject3\tests> pytest tests/test_register.py    - working

Generate the report(USE COMMAND PROMPT)
To generate the report from existing Allure results you can use the following command:

$ allure generate <directory-with-results>
The report will be generated to allure-report folder. You can change the destination folder using -o flag:

$ allure generate <directory-with-results> -o <directory-with-report>
For more information use the allure help generate command.

Open the report
When the report is generated you can open it in your default system browser. Simply run

$ allure open <directory-with-report>
You can also use allure serve command, to generate the report to temporary folder and open it.
Clean the report
If you want to remove the generated report data use allure report clean command.

By default the report commands will looking for the report in allure-results folder. If you are want to use the report
from different location you can use -o option.
