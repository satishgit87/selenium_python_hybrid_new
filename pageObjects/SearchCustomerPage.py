from selenium.webdriver.common.by import By

class SearchCustomer:
    txt_email_id = "SearchEmail"
    txt_firstName_id = "SearchFirstName"
    txt_lastName_id = "SearchLastName"
    btn_search_id = "search-customers"

    table_customers_id = "customers-grid"
    table_searchCustomer_row = "//table[@id='customers-grid']//tbody/tr"
    table_searchCustomer_column = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver
    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txt_email_id).clear()
        self.driver.find_element(By.ID, self.txt_email_id).send_keys(email)

    def setFirstName(self, fName):
        self.driver.find_element(By.ID, self.txt_firstName_id).clear()
        self.driver.find_element(By.ID, self.txt_firstName_id).send_keys(fName)

    def setLastName(self, lName):
        self.driver.find_element(By.ID, self.txt_lastName_id).clear()
        self.driver.find_element(By.ID, self.txt_lastName_id).send_keys(lName)

    def clickSearch(self):
        self.driver.find_element(By.ID, self.btn_search_id).click()

    def getTotalRows(self):
        return len(self.driver.find_elements(By.XPATH, self.table_searchCustomer_row))

    def getTotalCols(self):
        return len(self.driver.find_elements(By.XPATH, self.table_searchCustomer_column))

    def searchCustomerByEmail(self, email):
        flag = False

        for i in range(1, self.getTotalRows()+1):
            table = self.driver.find_element(By.ID, self.table_customers_id)
            emailId = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr[" + str(i) + "]/td[2]").text
            if emailId == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, customerName):
        flag = False

        for i in range(1, self.getTotalRows()+1):
            table = self.driver.find_element(By.ID, self.table_customers_id)
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr[" + str(i) + "]/td[3]").text
            if name == customerName:
                flag = True
                break
        return flag