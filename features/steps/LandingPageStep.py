from behave import *
from features.pages.LandingPageClass import LandingPageClass

@given("Launch Chrome Browser and Payback Application")
def step_impl(context):
    context.driver.implicitly_wait(2)
    expectedResult = "Largest Multi-brand Loyalty Program in India - PAYBACK"
    actualResult = context.driver.title
    assert (expectedResult == actualResult)
    context.driver.implicitly_wait(3)

@when("User clicks on Login Page icon")
def step_impl(context):
    context.driver.implicitly_wait(2)
    landingPage = LandingPageClass(context.driver)
    landingPage.click_login_icon()


@then(u'User is navigated to Login Page')
def step_impl(context):
    context.driver.implicitly_wait(3)
    expectedResult = "Login to your PAYBACK Account"
    actualResult = context.driver.title
    assert(expectedResult == actualResult)
    print(actualResult)
    context.driver.implicitly_wait(3)
