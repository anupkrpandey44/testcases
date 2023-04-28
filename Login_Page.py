from selenium.webdriver.common.by import By


class loginpage:
    textbox_username_id="username"
    textbox_password_id="password"
    button_submit_id="submit"
    button_logout_linktext="Log out"

    def __int__(self,driver):
        self.driver=driver
    def setUsername(self,username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)
    def setPassword(self,password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)
    def clickLogin(self):
        self.driver.find_element(By.ID, self.button_submit_id).click()
    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.button_logout_linktext).click()
