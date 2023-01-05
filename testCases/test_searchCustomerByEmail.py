import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_004_SearchCustomerByEmail():
    baseURL = ReadConfig.getApplicationUrl()
    userName = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.logGen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setUp):
        self.logger.info("********* Search customer by email 004 **********")
        self.driver = setUp
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******* Login successful *********")

        self.logger.info("******* Starting Search customer by Email *********")
        self.addCust = AddCustomer(self.driver)
        self.addCust.clickCustomersMenu()
        self.addCust.clickCustomerMenuItem()

        self.logger.info("******* Searching customer by Email *********")
        searchCust = SearchCustomer(self.driver)
        searchCust.setEmail("victoria_victoria@nopCommerce.com")
        searchCust.clickSearch()
        time.sleep(2)
        status = searchCust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("***** Search customer by email finished *******")

