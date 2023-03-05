from behave import *
from features.pages.JoinNowPageClass import JoinNowPageClass


@then(u'User is navigated to Join Now page')
def step_impl(context):
    context.driver.implicitly_wait(3)
    joinNowPage = JoinNowPageClass(context.driver)
    expectedResult = "Join Now"
    actualResult = joinNowPage.join_now_page()
    print(actualResult)
    assert (expectedResult == actualResult)
    context.driver.implicitly_wait(3)
