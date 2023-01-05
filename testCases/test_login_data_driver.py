import time

import pytest

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from utilities import ExcelUtils

class Test002DataDrivenLogin:
    baseURL = ReadConfig.getApplicationUrl()
    path = ".//testData/LoginData.xlsx"
    logger = LogGen.logGen()

    @pytest.mark.regression
    def testLoginDDT(self,setUp):
        self.logger.info("************ Test002DataDrivenLogin *****************")
        self.logger.info("************ Login DDT test is started *****************")
        self.driver = setUp
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        lst_status = []
        for i in range(2, self.rows+1):
            self.userName = ExcelUtils.readData(self.path, 'Sheet1',i,1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1',i,2)
            self.exp = ExcelUtils.readData(self.path, 'Sheet1',i,3)
            self.lp.setUserName(self.userName)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(2)
            actualTitle = self.driver.title

            if actualTitle == "Dashboard / nopCommerce administration":
                if self.exp == "PASS":
                    self.logger.info("************ PASSED *****************")
                    # self.lp.clickLogOut()
                    lst_status.append("Pass")
                elif self.exp == "FAIL":
                    self.logger.info("************ FAILED *****************")
                    # self.lp.clickLogOut()
                    lst_status.append("FAIL")
            elif actualTitle != "Dashboard / nopCommerce administration":
                if self.exp == "PASS":
                    self.logger.info("************ FAILED *****************")
                    # self.lp.clickLogOut()
                    lst_status.append("FAIL")
                elif self.exp == "FAIL":
                    self.logger.info("************ PASSED *****************")
                    # self.lp.clickLogOut()
                    lst_status.append("PASS")

            if "FAIL" not in lst_status:
                self.logger.info(" ********** login DDT test passed **********")
                self.driver.close()
                assert True
            else:
                self.logger.info(" ********** login DDT test failed **********")
                self.driver.close()
                assert False
        self.logger.info("************ ENd of login DDT Test *****************")
        self.logger.info("************ Completed Test002DataDrivenLogin *****************")