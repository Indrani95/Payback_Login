from features.utility.UtilityClass import UtilityClass
def before_scenario(context, driver):
    UtilityClass.launch_browser(context)
    #context.driver.implicitly_wait(3)

    UtilityClass.maximize_browser_window(context)
    #context.driver.implicitly_wait(2)

    UtilityClass.launch_app(context)
    #context.driver.implicitly_wait(3)

def after_scenario(context, driver):

    UtilityClass.close_browser(context)
    #context.driver.implicitly_wait(3)
