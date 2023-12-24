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

@given('I should see Journal Submission Form')
def step_impl(context):
    form = context.browser.find_element(By.TAG_NAME, "form")
    assert form, f"Journal Submission Form expected, got {form} instead"

@when('I fill in Journal Submission Form with Title and Abstract')
def step_impl(context):
    journal_data = {"title" : "UNDERSTANDING INDIAN HOUSEHOLD’S SUSTAINABLE PRODUCT PURCHASE BEHAVIOUR: MARKET BASKET ANALYSIS",
                    "abstract" : "The comprehension of customer preferences regarding sustainable product types enables the identification of nuanced consumer inclinations, facilitating the evaluation of the specific sustainable product categories that customers are more likely to adopt."}
    
    title_input = context.browser.find_element(By.ID, "title")
    abstract_input = context.browser.find_element(By.ID, "abstract")
    
    title_input.send_keys(journal_data['title'])
    abstract_input.send_keys(journal_data['abstract'])

@when('I press Save and Continue')
def step_impl(context):
    submit_btn = context.browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_btn.click()

@then('I should see Recommendation Reviewer Page')
def step_impl(context):
    assert context.browser.current_url == 'http://localhost:8000/reviewer/submission', f"Expected Recommendation Reviewer Page, but got {context.browser.current_url}"
    

@then('I should see list of recommended reviewer')
def step_impl(context):
    recommendations = context.browser.find_element(By.CLASS_NAME, "journal")
    assert recommendations, f"List of recomended reviewer expected, got {recommendations}"
