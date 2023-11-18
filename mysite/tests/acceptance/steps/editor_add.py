from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from django.test import Client
from selenium import webdriver

@when("I am on Add Account Page")
def step_impl(context):
    context.client = Client()
    context.browser = webdriver.Chrome()
    