# pytest_selenium_automation

Prerequisites:
1. Install Python 3.8 and above and Set the ENV Path for the Python executable
2. Make sure that Chrome/Firefox browser installed
3. Install the below-mentioned python packages
	pytest (7.1.1)
	pytest-html (3.1.1)
	selenium (4.1.3)
	webdriver-manager (3.5.4)

4. Modify the testConfig/settings.py file for browser, URL and user-related information

Execution steps:
-----------------
Go to the Project1 main folder and execute
	Ex: python -m pytest --html Reports/report.html  .\testCases\test.py
 
