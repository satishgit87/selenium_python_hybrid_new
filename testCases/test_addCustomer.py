import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationUrl()
    userName = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.logGen()

    @pytest.mark.sanity
    def test_addCustomer(self, setUp):
        self.logger.info("************************ Test_003_AddCustomer ************************")
        self.driver = setUp
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**********************Login Successful ***********************")

        self.logger.info("********************** Starting Add Customer Test ***********************")

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickCustomersMenu()
        self.addCust.clickCustomerMenuItem()
        self.addCust.clickAddNewBtn()
        time.sleep(2)

        self.logger.info("********************** Providing Customer Info ***********************")
        self.email = random_generator() + "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("123456")
        self.addCust.setCustomerRoles("Guests")
        self.addCust.setManagerofVendor("Vendor 2")
        self.addCust.setGender("Male")
        self.addCust.setFirstName("Gullapudi")
        self.addCust.setLastName("Satish Kumar")
        self.addCust.setDOB("1/1/1985")
        self.addCust.setCompanyName("TestCompany")
        self.addCust.setAdminContent("Testing content......")
        self.addCust.clickSave()

        self.logger.info("********************** Saving Customer Info ***********************")

        self.logger.info("********************** ADD CUSTOMER VALIDATION STARTED ***********************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        if "customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("************ ADD CUSTOMER TEST PASSED **************")
        else:
            self.driver.save_screenshot(".\\screenshots\\test_addCustomer_scr.png")
            self.logger.error("*********** Add customer test failed ************")
            assert True == False
        self.driver.close()
        self.logger.info(("*************** Ending Home Page Title Test **************"))

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))