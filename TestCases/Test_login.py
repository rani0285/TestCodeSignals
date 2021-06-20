import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utility.customLogger import LogGen


# from configurations.config import TestData


class Test_001_Login:
    baseUrl = "https://app.codesignal.com/public-test/3sxbxzafCYJiD7yix/pdWADxrwXHaH35"
    Email = "bruce.wayne@codesignal.com"
    FullName = "Bruce wayne"
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("*************Test_001_Login************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "CodeSignal":
            assert True
        else:
            assert False

    def test_login(self, setup):
        self.logger.info("*************verifying Login Test************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.Email)
        self.lp.setFullName(self.FullName)
        self.lp.clickCheckBox()
        self.lp.clickButtonQuickSignUp()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "CodeSignal":
            assert True
        else:
            assert False

    def test_ClickOnButtonSignUpWithFacebook(self, setup):
        self.logger.info("*************verifying SignUpWithFacebook ************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.ClickOnButtonSignUpWithFacebook()
        text = self.driver.find_element_by_xpath("//*[@id='homelink']").text
        self.driver.close()
        if text == "Facebook":
            assert True
        else:
            assert False

    def test_ClickOnButtonSignUpWithGoogle(self, setup):
        self.logger.info("*************verifying SignUpWithGoogle ************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.ClickOnButtonSignUpWithGoogle()
        text = self.driver.find_element_by_xpath("//*[@class='kHn9Lb']").text
        self.driver.close()
        if text == "Sign in with Google":
            assert True
        else:

            assert False

    def test_ClickOnButtonSignUpWithGitHub(self, setup):
        self.logger.info("*************verifying SignUpWithGitHub************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.ClickOnButtonSignUpWithGitHub()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Sign in to GitHub · GitHub":
            assert True
        else:
            assert False

    def test_ClickOnButtonSignUpWithTwitter(self, setup):
        self.logger.info("*************verifying SignUpWithTwitter************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.ClickOnButtonSignUpWithTwitter()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Twitter / Authorize an application":
            assert True
        else:
            assert False

    def test_ClickOnButtonSignUpWithPassword(self, setup):
        self.logger.info("*************verifying SignUpWithPassword************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.ClickOnButtonSignUpWithPassword()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "CodeSignal":
            assert True
        else:
            assert False

    def test_ClickOnButtonSignIn(self, setup):
        self.logger.info("*************verifying SignIn************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.ClickOnButtonSignIn()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "CodeSignal":
            assert True
        else:
            assert False
