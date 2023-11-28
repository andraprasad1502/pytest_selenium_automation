from selenium import webdriver as wb
from selenium.webdriver.common.by import By


class LoginPage:

    def enter_user_name(self, username):
        self.driver.find_element(By.NAME, "email").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, "password").send_keys(password)

    def submit_login(self):
        self.driver.find_element(By.XPATH, "//button[text()='Log in']").submit()
