from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from django.test import Client
from selenium import webdriver
# from common_steps import *

@given("i am on List Reviewer Page")
def step_impl(context):
    context.client = Client()
    context.browser = webdriver.Chrome()  # Use the appropriate WebDriver for your browser
    context.browser.get('http://localhost:8000/reviewer/')

# @given("and i should see list reviewer")
# def step_impl(context):

@when("i press Edit button on one reviewer from List Reviewer")
def step_impl(context):
    edit_button = context.browser.find_element(By.CLASS_NAME, 'bi-pencil-square')
    edit_button.click()

@when("i see edit reviewer form")
def step_impl(context):
    pass

@when("i fill in Edit Reviewer Form with the latest data")
def step_impl(context):
    context.update_data = {'name': 'Reviewer1', 'email': 'Reviewer1@gmail.com', 'scopus_id': '12345678', 'scholar_id': 'qytTHTMAAAAJ'}

    # name_input = context.browser.find_element(By.CLASS_NAME, 'fullname')
    # email_input = context.browser.find_element (By.CLASS_NAME, 'email')
    ScopusID_input = context.browser.find_element (By.CLASS_NAME, 'scopus_id')
    ScholarID_input = context.browser.find_element (By.CLASS_NAME,'scholar_id')
    
    # name_input.send_keys(context.update_data['name'])
    # email_input.send_keys(context.update_data['email'])
    ScopusID_input.send_keys(context.update_data['scopus_id'])
    ScholarID_input.send_keys(context.update_data['scholar_id'])

@when("i press save edit")
def step_impl(context):
    save_button = context.browser.find_element(By.CLASS_NAME, 'btn-simpan')
    save_button.click()

@when("i press Cancel")
def step_impl(context):
    cancel_button = context.browser.find_element(By.CLASS_NAME,'btn-cancel')
    cancel_button.click()
    
@then ("the response should contain Success")
def step_impl(context):
    success = context.browser.find_element(By.CLASS_NAME, 'success')
    assert success, f"Expected 'Update Account Success' in page source, but got {success}"


@then("i should be on list reviewer page")
def step_impl(context):
    context.browser.get('http://localhost:8000/reviewer/') #gtw