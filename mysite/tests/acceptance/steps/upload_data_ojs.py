from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from django.test import Client
from selenium import webdriver

@given("I am on Upload Data OJS Page")
def step_impl(context):
    context.client = Client()
    context.webdriver = webdriver.Chrome()
    
    
@given("I see Upload OJS Form")
def step_impl(context):
    context.browser.get('http://127.0.0.1:8000/upload-ojs/')

@when("I attach the file DataOJS.xlsx to Upload OJS Form")
def step_impl(context):
    file = open('../file/USERS JISEBI.xlsx')
    