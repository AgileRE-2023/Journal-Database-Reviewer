import django.contrib
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from django.test import Client
from selenium import webdriver
from faker import Faker

# @given("I am on List Reviewer Page")
# def step_impl(context):
#     context.client  = Client()
#     context.browser = webdriver.Chrome()
#     context.browser.get('http://127.0.0.1:8000/reviewer/')

# @given("And i see list reviewer")
# def step_impl(context):

@when ("I press Add button")
def step_impl(context):
    add_button = context.browser.find_element(By.CLASS_NAME, 'btn-tambah')

@when ("i see add reviewer form")
def step_impl(context):
    add_button = context.browser.find_element(By.CLASS_NAME, 'btn-tambah')
    add_button.click()
    # context.browser.get('http://127.0.0.1:8000/reviewer/')

@when ("i fill in Add Reviewer Form with full Name, Email, Scopus ID, dan Scholar ID")
def step_impl(context):
    fake = Faker(['id_ID'])
    context.add_data = {'name': fake.name(), 'email': fake.ascii_email(), 'scopus_id': '57204106663', 'scholar_id': 'qytTHTMAAAAJ'}
    # context.browser.get('http://127.0.0.1:8000/reviewer/')

    name_input = context.browser.find_element(By.CLASS_NAME, 'fullname')
    email_input = context.browser.find_element (By.CLASS_NAME, 'email')
    ScopusID_input = context.browser.find_element (By.CLASS_NAME, 'scopus_id')
    ScholarID_input = context.browser.find_element (By.CLASS_NAME,'scholar_id')
    
    name_input.send_keys(context.add_data['name'])
    email_input.send_keys(context.add_data['email'])
    ScopusID_input.send_keys(context.add_data['scopus_id'])
    ScholarID_input.send_keys(context.add_data['scholar_id'])
    
@when ("i fill in Add Reviewer Form with full Name, Email that already exist, Scopus ID, dan Scholar ID")
def step_impl(context):
    fake = Faker(['id_ID'])
    context.add_data = {'name': fake.name(), 'email': 'reviewer1@gmail.com', 'scopus_id': '57204106663', 'scholar_id': 'qytTHTMAAAAJ'}
    # context.browser.get('http://127.0.0.1:8000/reviewer/')

    name_input = context.browser.find_element(By.CLASS_NAME, 'fullname')
    email_input = context.browser.find_element (By.CLASS_NAME, 'email')
    ScopusID_input = context.browser.find_element (By.CLASS_NAME, 'scopus_id')
    ScholarID_input = context.browser.find_element (By.CLASS_NAME,'scholar_id')
    
    name_input.send_keys(context.add_data['name'])
    email_input.send_keys(context.add_data['email'])
    ScopusID_input.send_keys(context.add_data['scopus_id'])
    ScholarID_input.send_keys(context.add_data['scholar_id'])

@when ("i press Save")
def step_impl(context):
    save_button = context.browser.find_element(By.CLASS_NAME, 'btn-simpan')
    save_button.click()

@then ("the response should contain add success")
def step_impl(context):
    success = context.browser.find_element(By.CLASS_NAME, 'success')
    assert success, f"Expected 'Add Account Success' in page source, but got {success}"

# @then("I should be on Dashboard")
# def step_impl(context):
#     context.browser.get('http://localhost:8000/editor/dashboard/')
#     assert context.browser.current_url == 'http://localhost:8000/editor/dashboard/', f"Expected dashboard page, but got {context.browser.current_url}"

@then("The response should contain Reviewer with this email already exist")
def step_impl(context):
    message = context.browser.find_element(By.CLASS_NAME, 'error')
    assert message, f"Expected 'Reviewer with this email already exist' not in page source, but got {message}"

# @then ("i should be on list reviewer page")
# def step_impl(context):
#     context.browser.get('http://127.0.0.1:8000/reviewer/')