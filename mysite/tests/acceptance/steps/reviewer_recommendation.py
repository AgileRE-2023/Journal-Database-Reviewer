from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from django.test import Client
from selenium import webdriver

from behave import given, when, then

@given('I am on Search Recommendation Reviewer Page')
def step_impl(context):
    context.client = Client()
    context.browser = webdriver.Chrome()
    
    context.browser.get("http://localhost:8000/reviewer/submission")

@when('I should see Journal Submission Form')
def step_impl(context):
    form = context.browser.find_element(By.TAG_NAME, "form")
    assert form, f"Journal Submission Form expected, got {form} instead"

@when('I fill in Journal Submission Form with Title and Abstract')
def step_impl(context):
    # Your implementation for filling in the Journal Submission Form
    pass

@when('I press Save and Continue')
def step_impl(context):
    # Your implementation for pressing Save and Continue
    pass

@then('I should see Recommendation Reviewer Page')
def step_impl(context):
    # Your implementation for checking if the Recommendation Reviewer Page is visible
    pass

@then('I should see list of recommended reviewer')
def step_impl(context):
    # Your implementation for checking the presence of the recommended reviewer list
    pass
