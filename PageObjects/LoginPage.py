from selenium import webdriver


class LoginPage:
    textbox_Email_id = "input-1"
    textbox_FullName_id = "input-2"
    checkbox_privacy_xpath = "//div[@role='button']//div[@class='button--content -layout-h -center-center -space-h-8']//div[@class='icon -size-20']//div[@class='-layout-h -center']"

    button_QuickSignUp_xpath = "//div[@data-name='signup']"
    button_SignUpWithFaceBook_xpath = "//div[@data-name='auth-facebook']"
    button_SignUpWithGoogle_xpath = "//div[@data-name='auth-google']"
    button_SignUpWithGitHub_xpath = "//div[@data-name='auth-github']"
    button_SignUpWithTwitter_xpath = "//div[@data-name='auth-twitter']"
    button_SignUpWithPassword_xpath = "//div[@data-name='auth-password']"
    button_SignIn_Xpath = "//div[@data-name='switch-pages']"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, Email):
        self.driver.find_element_by_id(self.textbox_Email_id).clear()
        self.driver.find_element_by_id(self.textbox_Email_id).send_keys(Email)

    def setFullName(self, FullName):
        self.driver.find_element_by_id(self.textbox_FullName_id).clear()
        self.driver.find_element_by_id(self.textbox_FullName_id).send_keys(FullName)

    def clickCheckBox(self):
        self.driver.find_element_by_xpath(self.checkbox_privacy_xpath).click()

    def clickButtonQuickSignUp(self):
        self.driver.find_element_by_xpath(self.button_QuickSignUp_xpath).click()

    def ClickOnButtonSignUpWithFacebook(self):
        self.driver.find_element_by_xpath(self.button_SignUpWithFaceBook_xpath).click()

    def ClickOnButtonSignUpWithGoogle(self):
        self.driver.find_element_by_xpath(self.button_SignUpWithGoogle_xpath).click()

    def ClickOnButtonSignUpWithGitHub(self):
        self.driver.find_element_by_xpath(self.button_SignUpWithGitHub_xpath).click()

    def ClickOnButtonSignUpWithTwitter(self):
        self.driver.find_element_by_xpath(self.button_SignUpWithTwitter_xpath).click()

    def ClickOnButtonSignUpWithPassword(self):
        self.driver.find_element_by_xpath(self.button_SignUpWithPassword_xpath).click()

    def ClickOnButtonSignIn(self):
        self.driver.find_element_by_xpath(self.button_SignIn_Xpath).click()

