from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from django.test import Client
from selenium import webdriver

@given("I am on Login Page")
def step_impl(context):
    context.client = Client()
    context.browser = webdriver.Chrome()  # Use the appropriate WebDriver for your browser

@when("I fill in Login Form with correct email and password")
def step_impl(context):
    context.login_data = {'email': 'editor1@email.com', 'password': 'editor123'}  # Update with your test data
    context.browser.get('http://localhost:8000/signin/')  # Update with your Django development server URL

    # Example: Use Selenium to fill in form fields
    email_input = context.browser.find_element(By.ID, 'id_email')
    password_input = context.browser.find_element(By.ID, 'id_password')

    email_input.send_keys(context.login_data['email'])
    password_input.send_keys(context.login_data['password'])
    
@when("I fill in Login Form with incorrect email and password")
def step_impl(context):
    context.login_data = {'email': 'noteditor@email.com', 'password': 'noteditor123'}  # Update with your test data
    context.browser.get('http://localhost:8000/signin/')  # Update with your Django development server URL

    # Example: Use Selenium to fill in form fields
    email_input = context.browser.find_element(By.ID, 'id_email')
    password_input = context.browser.find_element(By.ID, 'id_password')

    email_input.send_keys(context.login_data['email'])
    password_input.send_keys(context.login_data['password'])

@when("I press Login button")
def step_impl(context):
    # Example: Use Selenium to click the login button
    login_button = context.browser.find_element(By.CLASS_NAME, 'loginBtn')
    login_button.click()

@then("the response should not contain Login Success")
def step_impl(context):
    assert "Login Success" not in context.browser.page_source, f"Expected 'Login Success' not in page source, but got {context.browser.page_source}"

@then("I should be on Dashboard")
def step_impl(context):
    # Implement code to check if the current page is the dashboard
    context.browser.get('http://localhost:8000/editor/dashboard/')
    assert context.browser.current_url == 'http://localhost:8000/editor/dashboard/', f"Expected dashboard page, but got {context.browser.current_url}"

@then("I should be on Login Page")
def step_impl(context):
    # Implement code to check if the current page is the login page
    assert context.browser.current_url == 'http://localhost:8000/signin/', f"Expected login page, but got {context.browser.current_url}"

@then("close the browser")
def step_impl(context):
    context.browser.quit()


# use_step_matcher("re")

# @given("I am on Login Page")
# def step_impl(context):
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     context.selenium = webdriver.Chrome(options=chrome_options)
    
#     context.selenium.get(f'{context.test.live_server_url}/signin')
    
# @when("I fill in Login form with correct email and password")
# def step_impl(context):
#     email = 'editor1@gmail.com'
#     password = 'editor123'
#     iEmail = context.selenium.find_element_by_id("id_email")
#     iEmail.send_keys(email)
#     iPassword = context.selenium.find_element_by_id("id_password")
#     iPassword.send_keys(password)
    
# @when("I press Login button")
# def step_impl(context):
#     login_button = context.selenium.find_element_by_name('loginBtn')
#     login_button.click()
    
# @then("The response should contain 'Login Success'")
# def step_impl(context):
#     assert "Login Success" in context.selenium.page_source, f'Expected Login Success in page source, but got {context.selenium.page_source}'
    
# @then("The response should not contain 'Login Success'")
# def step_impl(context):
#     assert "Login Success" not in context.selenium.page_source, f'Expected Login Success not in page source, but got {context.selenium.page_source}'
    
# @then("I should be on Dashboard")
# def step_impl(context):
#     assert context.selenium.current.url == 'http://127.0.0.1:8000/editor/dashboard'
    
# @then("I should be on Login Page")
# def step_impl(context):
#     assert context.selenium.current.url == 'http://127.0.0.1:8000/signin'
    
    