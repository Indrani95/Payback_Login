#Steps for LoginPage_DDF (Excel)

#valid data testing output = Hi, 'UserName'

from behave import *
from features.pages.LoginPageClass import LoginPageClass
from features.utility.UtilityClass import ConfigClass
from datafiles.Excelutils import ExcelUtils


@when("User enters {cn} and {pn} for first dataset")
def step_impl(context, cn, pn):
    context.driver.implicitly_wait(50)
    loginpage =LoginPageClass(context.driver)
    ExcelUtils.get_row_count(ConfigClass.dataFile, "Sheet1")
    cn = ExcelUtils.read_data(ConfigClass.dataFile, "Sheet1", 2, 1)
    pn = ExcelUtils.read_data(ConfigClass.dataFile, "Sheet1", 2, 2)
    loginpage.enter_card_number(cn)
    loginpage.enter_pin_number(pn)

@then("Then It shows home page for first dataset")
def step_impl(context):
    context.driver.implicitly_wait(50)
    loginpage = LoginPageClass(context.driver)
    expectedResult = True
    actualResult = loginpage.find_username()

    try:
        if (expectedResult == actualResult):
            assert True
            print("Test is passed")
            ExcelUtils.write_data(ConfigClass.dataFile, "Sheet1", 2, 3, loginpage.display_user_name())
            ExcelUtils.write_data(ConfigClass.dataFile, "Sheet1", 2, 4, "Passed")
            context.driver.implicitly_wait(50)
        else:
            print("Test is failed")
            ExcelUtils.write_data(ConfigClass.dataFile, "Sheet1", 2, 3, "False")
            ExcelUtils.write_data(ConfigClass.dataFile, "Sheet1", 2, 4, "Failed")
            assert False
        context.driver.implicitly_wait(50)
    finally:
        context.driver.implicitly_wait(50)
        loginpage.mouse_hover()
        loginpage.logout_user()
        print()

#invalid data testing, output = Error

@when("User enters {cn} and {pn} from invalid first dataset")
def step_impl(context, cn, pn):
    context.driver.implicitly_wait(50)
    loginpage =LoginPageClass(context.driver)
    ExcelUtils.get_row_count(ConfigClass.dataFile, "Sheet2")
    cn = ExcelUtils.read_data(ConfigClass.dataFile, "Sheet2", 2, 1)
    pn = ExcelUtils.read_data(ConfigClass.dataFile, "Sheet2", 2, 2)
    loginpage.enter_card_number(cn)
    loginpage.enter_pin_number(pn)


@then("It shows Error window for first data")
def step_impl(context):

    context.driver.implicitly_wait(50)
    loginpage = LoginPageClass(context.driver)
    actualResult = loginpage.error_window()
    expectedResult = "ERROR"
    print(actualResult)

    try:
        if (expectedResult == actualResult):
            assert True
            print("Test is passed")
            ExcelUtils.write_data(ConfigClass.dataFile, "Sheet2", 2, 3, actualResult)
            ExcelUtils.write_data(ConfigClass.dataFile, "Sheet2", 2, 4, "Passed")
            context.driver.implicitly_wait(50)
        else:
            print("Test is failed")
            ExcelUtils.write_data(ConfigClass.dataFile, "Sheet2", 2, 3, "False")
            ExcelUtils.write_data(ConfigClass.dataFile, "Sheet2", 2, 4, "Failed")
            assert False
        context.driver.implicitly_wait(50)
    finally:
        context.driver.implicitly_wait(1)
        print()

