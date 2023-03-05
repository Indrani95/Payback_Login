from selenium.webdriver.common.by import By
class JoinNowPageClass:

    def __init__(self, driver):
        self.driver = driver
        self.joinnowElement = "//h4[text()='Join Now']"

    def join_now_page(self):

        joinNowNavigation = self.driver.find_element(By.XPATH, self.joinnowElement)
        joinNowValue = joinNowNavigation.text
        return joinNowValue

