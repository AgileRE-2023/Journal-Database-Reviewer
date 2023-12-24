from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from django.test import Client
from selenium import webdriver

# @given("i am on Dashboard")
# def step(context):
#     context.client  = Client()
#     context.browser = webdriver.Chrome()
    
#     context.login_data = {'email': 'editor1@gmail.com', 'password': 'editor123'}
#     context.browser.get('http://localhost:8000/signin/') 

#     # Example: Use Selenium to fill in form fields
#     email_input = context.browser.find_element(By.ID, 'id_email')
#     password_input = context.browser.find_element(By.ID, 'id_password')

#     email_input.send_keys(context.login_data['email'])
#     password_input.send_keys(context.login_data['password'])
#     login_button = context.browser.find_element(By.CLASS_NAME, 'loginBtn')
#     login_button.click()
#     # context.browser.get("http://127.0.0.1:8000/editor/dashboard")
    
@given("i see Reviewer Scrapping")
def step(context):
    allHeader = context.browser.find_elements(By.TAG_NAME, "header")
    elements = []
    for e in allHeader:
        elements.append(e.text)
    
    assert "Reviewer Scraping" in elements, f"Expected Reviewer Scrapping in page source"
    
@when("i press Go")
def step(context):
    goBtn = context.browser.find_element(By.CLASS_NAME, "reviewer-btn")
    goBtn.click()
    
@then("The response should contain Scrapping Success")
def step(context):
    message = context.browser.find_element(By.CLASS_NAME, "success")
    assert message , f"Response should contain Upload Success, got {message}"