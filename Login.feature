Feature: Login into GLO account and extract employee's date of joining company

Scenario Outline: Login into account, find employee and extract date of joining company

	Given 	User navigates to GLO login website
	When 	User enters a username: "<username>"
	When 	User enters a password: "<password>"
	When 	User clicks on the login button
	When 	User closes the pop up message
	When 	User enters employee name in a search box: "<emp_name>""<emp_surname>"
	#When 	User clicks desired employee: "<emp_name>""<emp_surname>"
	When 	User should be taken to employee page: "<emp_name>""<emp_surname>"
	Then 	User should see employee's date of joining to the company and eventually the correct total experience


Examples: Test data
|username			|password	|emp_name		|emp_surname|
|employee.emp		|example1#	|example 		|example	|

