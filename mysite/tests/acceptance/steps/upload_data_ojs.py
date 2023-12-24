import django.contrib.auth
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from django.test import Client
from selenium import webdriver

import os

@given("I am on Upload Data OJS Page")
def step_impl(context):
    context.client = Client()
    context.browser = webdriver.Chrome()  
    
    context.login_data = {'email': 'editor1@gmail.com', 'password': 'editor123'}
    context.browser.get('http://localhost:8000/signin/') 

    email_input = context.browser.find_element(By.ID, 'id_email')
    password_input = context.browser.find_element(By.ID, 'id_password')

    email_input.send_keys(context.login_data['email'])
    password_input.send_keys(context.login_data['password'])
    
    login_button = context.browser.find_element(By.CLASS_NAME, 'loginBtn')
    login_button.click()
    
@given("I see Upload OJS Form")
def step_impl(context):
    context.browser.get('http://127.0.0.1:8000/upload-ojs/')
    # assert True

@when("I attach the file DataOJS.xlsx to Upload OJS Form")
def step_impl(context):
    
    context.browser.get('http://localhost:8000/upload-ojs/')
    file_path = 'file/USERS JISEBI.xlsx'
    upload_file = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", file_path)
    )
    
    file_input = context.browser.find_element(By.ID, "myFile")
    file_input.send_keys(upload_file)
    
@when("I attach the file DataOJS.pdf to Upload OJS Form")
def step_impl(context):
    context.browser.get('http://localhost:8000/upload-ojs/')
    file_path = 'file/DataOJS.pdf'
    upload_file = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", file_path)
    )
    
    file_input = context.browser.find_element(By.ID, "myFile")
    file_input.send_keys(upload_file)

@when("I attach the file DataOJS.xlsx to Upload OJS Form in wrong format")
def step_impl(context):
    context.browser.get('http://localhost:8000/upload-ojs/')
    file_path = 'file/DataOJS.xlsx'
    upload_file = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", file_path)
    )
    
    file_input = context.browser.find_element(By.ID, "myFile")
    file_input.send_keys(upload_file)
    
    # breakpoint()
    
    
# @when("I press Save and Continue")
# def step_impl(context):
#     context.browser.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    
@then("The response should contain Upload Success")
def step_impl(context):
    message = context.browser.find_element(By.CLASS_NAME, "success")
    assert message , f"Response should contain Upload Success, got {message}"
    
@then("The response should contain Upload Error")
def step_impl(context):
    message = context.browser.find_element(By.CLASS_NAME, "error")
    assert message , f"Response should contain Upload Error, got {message}"
    
@then("The response should contain Upload Failed")
def step_impl(context):
    message = context.browser.find_element(By.CLASS_NAME, "info")
    assert message, f"Response should contain Upload Failed, got {message}"
    
@then("I should be on Upload Data OJS Page")
def step_impl(context):
    assert context.browser.current_url == 'http://localhost:8000/upload-ojs/', f"Expected Upload Data OJS Page, but got {context.browser.current_url}"


    