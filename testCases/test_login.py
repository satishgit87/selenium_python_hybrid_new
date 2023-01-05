import time

import pytest

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage

class Test001Login:
    baseURL = ReadConfig.getApplicationUrl()
    userName = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.logGen()

    @pytest.mark.regression
    def testHomePageTitle(self, setUp):
        self.logger.info("************ Test001Login *****************")
        self.logger.info("************ Home Page title verification *****************")
        self.driver = setUp
        self.driver.get(self.baseURL)
        actualTitle = self.driver.title

        if actualTitle == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************ Home Page Title test is PASSED *****************")
        else:
            self.driver.save_screenshot(".\\screenshots\\testHomePageTitle.png")
            self.driver.close()
            self.logger.error("************ Home Page Title test is FAILED *****************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def testLogin(self,setUp):
        self.logger.info("************ Login test is started *****************")
        self.driver = setUp
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(2)
        actualTitle = self.driver.title

        if actualTitle == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************ Login test is PASSED *****************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\testLogin.png")
            self.driver.close()
            self.logger.error("************ Login test is FAILED *****************")
            assert False
