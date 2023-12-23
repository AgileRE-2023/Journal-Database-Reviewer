from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from django.test import Client
from selenium import webdriver

@given("i am on Dashboard")
def step(context):
    context.client  = Client()
    context.browse = webdriver.Chrome()
    
    context.browser.get("http://localhost:8000/editor/dashboard/")
    
@given("I see Reviewer Scrapping")
def step(context):
    # allHeader = context.browser.find_element(By.TAG_NAME, "header")
    assert "Reviewer Scrapping" in context.browser.page_source, f"Expected Reviewer Scrapping in page source"
    
@when("i press Go")
def step(context):
    goBtn = context.browser.find_element(By.CLASS_NAME, "reviewer-btn")
    goBtn.click()
    
@then("The response should contain Scrapping Success")
def step(context):
    message = context.browser.find_element(By.CLASS_NAME, "success")
    assert message , f"Response should contain Upload Success, got {message}"