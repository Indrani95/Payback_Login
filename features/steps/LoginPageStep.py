from behave import *
import time
from hamcrest import *
from features.pages.LoginPageClass import LoginPageClass


@when(u'User clicks on Sign Up #Payback Chalao Picture')
def step_impl(context):
    context.driver.implicitly_wait(50)
    loginPage = LoginPageClass(context.driver)
    loginPage.click_signup_image()

@when(u'User clicks on login button')
def step_impl(context):
    context.driver.implicitly_wait(50)
    loginPage = LoginPageClass(context.driver)
    loginPage.click_login_button()

@when(u'User enters {number} in PAYBACK card number or Mobile Number field')
def step_impl(context, number):
    context.driver.implicitly_wait(50)
    loginPage = LoginPageClass(context.driver)
    loginPage.enter_card_number(number)

@step("User enters {pin} in Pin field")
def step_impl(context, pin):
    context.driver.implicitly_wait(50)
    loginPage = LoginPageClass(context.driver)
    loginPage.enter_pin_number(pin)


@then(u'Login Button is Clickable')
def step_impl(context):
    context.driver.implicitly_wait(50)
    loginPage = LoginPageClass(context.driver)
    print(loginPage.login_clickable())
    assert (loginPage.login_clickable() == True)
    context.driver.implicitly_wait(50)


@then(u'User Logins Successfully into Payback Account')
def step_impl(context):

    loginPage = LoginPageClass(context.driver)
    expectedResult = True
    actualResult = loginPage.find_username()
    assert_that(expectedResult, equal_to(actualResult))
    print(loginPage.display_user_name())


@when(u'User selects Check Box on reCAPTCHA')
def step_impl(context):
    context.driver.implicitly_wait(50)
    loginPage = LoginPageClass(context.driver)
    loginPage.select_check_box()
    time.sleep(45)

@then("It shows Error window")
def step_impl(context):
    context.driver.implicitly_wait(50)
    loginpage = LoginPageClass(context.driver)
    actualResult = loginpage.error_window()
    expectedResult = "ERROR"
    print(actualResult)
    assert (expectedResult == actualResult)
    context.driver.implicitly_wait(50)


@then(u'Payback Card Number field and Pin fields are Empty')
def step_impl(context):
    context.driver.implicitly_wait(50)
    loginpage = LoginPageClass(context.driver)
    expectedResult = True
    actualResult = loginpage.find_fields_empty()
    print(actualResult)
    assert (expectedResult == actualResult)
    context.driver.implicitly_wait(50)




