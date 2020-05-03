import behave


@behave.given('User navigates to GLO login website')
def user_navigates_to_website(context):
    context.loginPage.getPage()


@behave.when('User enters a username: "{username}"')
def user_enters_a_username(context, username):
    context.loginPage.putUsername(username)


@behave.when('User enters a password: "{password}"')
def user_enters_a_password(context, password):
    context.loginPage.putPassword(password)


@behave.when("User clicks on the login button")
def user_clicks_on_the_login_button(context):
    context.loginPage.clickLogin()


@behave.when('User closes the pop up message')
def user_closes_the_pop_up_message(context):
    context.homePage.closePopUp()


@behave.when('User enters employee name in a search box: "{emp_name}""{emp_surname}"')
def user_enters_employee_name_in_a_search_box(context, emp_name, emp_surname):
    context.homePage.putEmployeeName(emp_name, emp_surname)


@behave.when('User clicks desired employee: "{emp_name}""{emp_surname}"')
def user_clicks_desired_employee(context, emp_name, emp_surname):
    context.searchEmployeeResultsPage.chooseEmployee(emp_name, emp_surname)


@behave.when('User should be taken to employee page: "{emp_name}""{emp_surname}"')
def user_should_be_taken_to_employee_page(context, emp_name, emp_surname):
    assert context.employeePage.employeePageCheck(emp_name, emp_surname) is True


@behave.then('User should see employee\'s date of joining to the company and eventually the correct total experience')
def user_should_be_taken_to_employee_page(context):
    assert context.employeePage.checkEmployeeDateOfJoining() is True
