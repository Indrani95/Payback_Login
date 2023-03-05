from selenium.webdriver.common.by import By
class LandingPageClass:

    def __init__(self, driver):
        self.driver = driver
        self.loginIconElement = "//a[@data-clicktext='Login']"

    def click_login_icon(self):
        loginIconField = self.driver.find_element(By.XPATH, self.loginIconElement)
        loginIconField.click()


