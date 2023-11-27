from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from django.test import Client
from selenium import webdriver

@given("I am on List Reviewer Page")
def step_impl(context):
    context.client  = Client()
    context.browse = webdriver.Chrome()

@given("And i see list reviewer")
def step_impl(context):
    context.browser.get('http://127.0.0.1:8000/reviewer/')

@when ("I press Add button")
def step_impl(context):
    add_button = context.browser.find_element(By.CLASS_NAME, 'btn-tambah bi bi-plus-square')
    add_button.click()

@when ("And i see add reviewer form")
def step_impl(context):
    context.browser.get('http://127.0.0.1:8000/reviewer/')

@when ("And i fill in Add Reviewer Form with full Name, Email, Institution, Scopus ID, dan Scholar ID")
def step_impl(context):
    context.add_data = {'name': 'Reviewer1', 'email': 'Reviewer1@gmail.com', 'institution': 'Universitas Airlangga', 'Scopus ID': '57204106663', 'Scholar ID': 'qytTHTMAAAAJ'}
    context.browser.get('http://127.0.0.1:8000/reviewer/')

    name_input = context.browser.find_element(By.CLASS_NAME, 'fullname')
    email_input = context.browser.find_elemet (By.CLASS_NAME, 'email')
    institution_input = context.browser.find_element (By.CLASS_NAME, 'institution')
    ScopusID_input = context.browser.find_element (By.CLASS_NAME, 'scopus_id')
    ScholarID_input = context.browser.find_element (By.CLASS_NAME,'scholar_id')
    
    name_input.send_keys(context.add_data['name'])
    email_input.send_keys(context.add_data['email'])
    institution_input.send_keys(context.add_data['institution'])
    ScopusID_input.send_keys(context.add_data['scopus_id'])
    ScholarID_input.send_keys(context.add_data['scholar_id'])

@when ("And i press Save")
def step_impl(context):
    save_button = context.browser.find_element(By.CLASS_NAME, 'btn-simpan')
    save_button.click()

@then ("the response should contain add success")
def step_impl(context):
    success = context.browser.find_element(By.CLASS_NAME, 'success')
    assert success, f"Expected 'Add Account Success' in page source, but got {success}"

@then("I should be on Dashboard")
def step_impl(context):
    context.browser.get('http://localhost:8000/editor/dashboard/')
    assert context.browser.current_url == 'http://localhost:8000/editor/dashboard/', f"Expected dashboard page, but got {context.browser.current_url}"

@then("The response should not contain Add Success")
def step_impl(context):
    success = context.browser.find_element(By.CLASS_NAME, 'success').text.strip()
    assert "Add Success" in success , f"Expected 'Add Account Success' not in page source, but got {success}"

@then("The response should contain Reviewer already exist")
def step_impl(context):
    success = context.browser.find_element(By.CLASS_NAME, 'success').text.strip()
    assert "Add Account Success" in success , f"Expected 'Add Account Success' not in page source, but got {success}"

@then ("and i should be on list reviewer page")
def step_impl(context):
    context.browser.get('http://127.0.0.1:8000/reviewer/') #gtw masihan