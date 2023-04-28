import pytest
from selenium import webdriver
from PageObjects.Login_Page import loginpage

class LoginPage:
    URL= "https://practicetestautomation.com/practice-test-login/"
    username= "student"
    password= "Password123"

    def test_Title(self):
        self.driver=webdriver.Chrome()
        self.driver.get(self.URL)
        title=self.driver.title
        if title=="Test Login | Practice Test Automation":
            assert True
        else:
            assert False

    def test_logging_in(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)
        self.lpobj=loginpage(self.driver)
        self.lpobj.setUsername(self.username)
        self.lpobj.setPassword(self.password)
        self.lpobj.clickLogin()
        title=self.driver.title
        if title=="Logged In Successfully | Practice Test Automation":
            assert True
        else:
            assert False

    def test_logging_out(self):
        self.logoutobj=loginpage(self.driver)
        self.logoutobj.clickLogout()


