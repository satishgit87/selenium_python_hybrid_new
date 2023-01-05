import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_005_SearchCustomerByName():
    baseURL = ReadConfig.getApplicationUrl()
    userName = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.logGen()

    @pytest.mark.regression
    def test_searchCustomerByName(self, setUp):
        self.logger.info("********* Search customer by name 005 **********")
        self.driver = setUp
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******* Login successful *********")

        self.logger.info("******* Starting Search customer by Name *********")
        self.addCust = AddCustomer(self.driver)
        self.addCust.clickCustomersMenu()
        self.addCust.clickCustomerMenuItem()

        self.logger.info("******* Searching customer by Name *********")
        searchCust = SearchCustomer(self.driver)
        searchCust.setFirstName("Victoria")
        searchCust.setLastName("Terces")
        searchCust.clickSearch()
        time.sleep(2)
        status = searchCust.searchCustomerByName("Victoria Terces")
        assert True == status
        self.logger.info("***** Search customer by name finished *******")

