from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
class LoginPageClass:


    def __init__(self, driver):

        self.driver = driver

        self.signupElement = "//a[@class='sso-element ']"
        self.cardnumberFieldElement = "card_number"
        self.pinFieldElement = "pin_number"
        self.checkBoxElement = "//div[@class='recaptcha-checkbox-border']"

        self.loginButtonElement = "//button[text()='LOGIN']"
        self.frameElement = "iframe"

        self.joinnowElement = "//h4[text()='Join Now']"

        self.userNameElement = "//span[@class='pb-user-name']"
        self.errorElement = "//div[text()='ERROR']"

        self.mousehoverElement = "myUserbar"
        self.logoutElement = "//a[@class='pb-logout']"

    def enter_card_number(self, card_number):
        cardnumberField = self.driver.find_element(By.NAME, self.cardnumberFieldElement)
        cardnumberField.send_keys(card_number)

    def enter_pin_number(self, pin_number):
        pinField = self.driver.find_element(By.NAME, self.pinFieldElement)
        pinField.send_keys(pin_number)

    def select_check_box(self):
        frameField = self.driver.find_element(By.TAG_NAME, self.frameElement)
        self.driver.switch_to.frame(frameField)
        checkBoxField = self.driver.find_element(By.XPATH, self.checkBoxElement)
        checkBoxField.click()
        self.driver.switch_to.default_content()

    def click_login_button(self):
        loginButtonField = self.driver.find_element(By.XPATH, self.loginButtonElement)
        loginButtonField.click()

    def login_clickable(self):
        loginButtonField = self.driver.find_element(By.XPATH, self.loginButtonElement)
        if (loginButtonField.is_displayed() == True and loginButtonField.is_enabled() == True):
            return True
        return

    def click_signup_image(self):
        signUpPicture = self.driver.find_element(By.XPATH, self.signupElement)
        signUpPicture.click()
        print("Parent window title: " + self.driver.title)
        parent = self.driver.current_window_handle
        child = self.driver.window_handles

        for w in child:

            if (w != parent):
                self.driver.switch_to.window(w)
    def find_username(self):
        wait = WebDriverWait(self.driver, 50)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.userNameElement)))
        userName = self.driver.find_element(By.XPATH, self.userNameElement)
        userNameValue = userName.is_displayed()
        return userNameValue

    def display_user_name(self):
        userName = self.driver.find_element(By.XPATH, self.userNameElement)
        userNameValue = userName.text
        return userNameValue

    def error_window(self):
        wait = WebDriverWait(self.driver, 50)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.errorElement)))
        errorWindow = self.driver.find_element(By.XPATH, self.errorElement)
        errorvalue = errorWindow.text
        return errorvalue

    def find_fields_empty(self):
        cardNumberBox = self.driver.find_element(By.NAME, self.cardnumberFieldElement)
        pinBox = self.driver.find_element(By.NAME, self.pinFieldElement)

        cardNumberValue = cardNumberBox.get_attribute('value')
        pinBoxValue = pinBox.get_attribute('value')
        print(cardNumberValue)
        print(pinBoxValue)

        if (len(cardNumberValue) == 0 and len(pinBoxValue)==0):
            print("Fields are empty cardnumber'"+cardNumberValue+"' and pin number '"+pinBoxValue+"'")
            return True
        else:
            print("Fields contain values"+cardNumberValue+"and"+pinBoxValue)
            return False

    def mouse_hover(self):
        mouseHover = self.driver.find_element(By.ID, self.mousehoverElement)
        action = ActionChains(self.driver)
        action.move_to_element(mouseHover)
        action.perform()

    def logout_user(self):
        logOut = self.driver.find_element(By.XPATH, self.logoutElement)
        logOut.click()


