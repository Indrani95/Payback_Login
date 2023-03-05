from selenium import webdriver
from selenium.webdriver.common.by import By

from features.utility.ConfigClass import ConfigClass

class UtilityClass:

    def __init__(self, driver):
        self.driver = driver

    def launch_browser(self):
        self.driver = webdriver.Chrome(ConfigClass.filePath)

    def maximize_browser_window(self):
        self.driver.maximize_window()

    def launch_app(self):
        self.driver.get(ConfigClass.url)

    def close_browser(self):
        self.driver.quit()


