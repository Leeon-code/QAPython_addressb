from selenium import webdriver
from selenium.webdriver.common.by import By

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.NAME, "user").send_keys("%s" % username)
        wd.find_element(By.NAME, "pass").send_keys("%s" % password)
        wd.find_element(By.ID, "LoginForm").click()
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()