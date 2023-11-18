from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from django.test import Client
from selenium import webdriver
from faker import Faker
from password_generator import PasswordGenerator

@given("I am on Add Account Page")
def step_impl(context):
    context.client = Client()
    context.browser = webdriver.Chrome()
    
    admin = {'email' : 'admin1@gmail.com', 'password' : 'qwerty10'}
    
    context.browser.get('http://127.0.0.1:8000/admin/login/?next=/admin/')
    email = context.browser.find_element(By.ID, 'id_username')
    password = context.browser.find_element(By.ID, 'id_password')
    loginbtn = context.browser.find_element(By.CLASS_NAME, 'submit-row').find_element(By.TAG_NAME, 'input')
    
    email.send_keys(admin['email'])
    password.send_keys(admin['password'])
    loginbtn.click()
    

@when("I fill in Add Account Form with name, email, and password")
def step_impl(context):
    context.browser.get('http://127.0.0.1:8000/admin/master/editor/add/')
    fake = Faker(['id_ID'])
    pwo = PasswordGenerator()
    pwo.minlen = 8
    
    editor = {'email' : fake.ascii_email(), 'name' : fake.name(), 'password' : pwo.generate()}
    
    email = context.browser.find_element(By.ID, 'id_email')
    name = context.browser.find_element(By.ID, 'id_name')
    password1 = context.browser.find_element(By.ID, 'id_password1')
    password2 = context.browser.find_element(By.ID, 'id_password2')
    submitBtn = context.browser.find_element(By.CLASS_NAME, 'submit-row').find_element(By.TAG_NAME, 'input')
    
    email.send_keys(editor['email'])
    name.send_keys(editor['name'])
    password1.send_keys(editor['password'])
    password2.send_keys(editor['password'])
    
    # submitBtn.click()
    
@when("I press Save Button")
def step_impl(context):
    submitBtn = context.browser.find_element(By.CLASS_NAME, 'submit-row').find_element(By.TAG_NAME, 'input')
    submitBtn.click()
    
@then("The response should contain Add Account Success")
def step_impl(context):
    # assert True
    success = context.browser.find_element(By.CLASS_NAME, 'success')
    assert success , f"Expected 'Add Account Success' in page source, but got {success}"
    
@then("The response should not contain Add Account Success")
def step_impl(context):
    success = context.browser.find_element(By.CLASS_NAME, 'success').text.strip()
    assert "Add Account Success" in success , f"Expected 'Add Account Success' not in page source, but got {success}"
    
@then('i should be on Add Account Page')
def step_impl(context):
    context.browser.get('http://127.0.0.1:8000/admin/master/editor/add/')
    assert context.browser.current_url == 'http://127.0.0.1:8000/admin/master/editor/add/', f"Expected login page, but got {context.browser.current_url}"