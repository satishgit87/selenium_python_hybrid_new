import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)

class AddCustomer():
    lnkCustomer_menu_XPATH = "//a[@href='#']//p[contains(text(),'Customers')]"
    # lnkCustomers_menuitem_XPATH = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_XPATH = "//nav[@class='mt-2']/ul/li[4]//li[1]"
    btn_addnew_XPATH = "//a[normalize-space()='Add new']"
    textbox_email_XPATH = "//input[@id='Email']"
    textbox_password_XPATH = "//input[@id='Password']"
    textbox_firstname_XPATH = "//input[@id='FirstName']"
    textbox_lastname_XPATH = "//input[@id='LastName']"
    radiobtn_gender_male = "//input[@id='Gender_Male']"
    radiobtn_gender_female = "//input[@id='Gender_Female']"
    textbox_date_of_birth = "//input[@id='DateOfBirth']"
    textbox_company_name = "//input[@id='Company']"
    checkbox_istax_exempt = "//input[@id='IsTaxExempt']"

    dropdown_newsletter = "//div[@class='form-group row'][9]/div[2]"
    newsletterdrp_listitem1 = "//li[normalize-space()='Your store name']"
    newsletterdrp_listitem2 = "//li[normalize-space()='Test store 2']"

    dropdown_customer_roles = "//div[@class='form-group row'][10]/div[2]"
    custroledrp_listitem_administrators = "//li[normalize-space()='Administrators']"
    custroledrp_listitem_forummoderators = "//li[normalize-space()='Forum Moderators']"
    custroledrp_listitem_guests = "//li[normalize-space()='Guests']"
    custroledrp_listitem_registered = "//span[normalize-space()='Registered']"
    custroledrp_listitem_vendors = "//li[contains(text(),'Vendors')]"
    custroledrp_crossbtn_XPATH = "//span[@title='delete']"

    dropdown_managerofvendor_XPATH = "//select[@id='VendorId']"
    textbox_admin_comment_XPATH = "//textarea[@id='AdminComment']"
    btn_save_XPATH = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickCustomersMenu (self):
        self.driver.find_element(By.XPATH, self.lnkCustomer_menu_XPATH).click()
    def clickCustomerMenuItem (self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_XPATH).click()
    def clickAddNewBtn(self):
        self.driver.find_element(By.XPATH, self.btn_addnew_XPATH).click()
    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.textbox_email_XPATH).send_keys(email)
    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_XPATH).send_keys(password)
    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.dropdown_customer_roles).click()
        time.sleep(2)
        if role == "Registered":
            self.listItem = self.driver.find_element(By.XPATH, self.custroledrp_listitem_registered)
        elif role == "Administrators":
            self.listItem = self.driver.find_element(By.XPATH, self.custroledrp_listitem_administrators)
        elif role == "Guests":
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.custroledrp_crossbtn_XPATH).click()
            self.listItem = self.driver.find_element(By.XPATH, self.custroledrp_listitem_guests)
        elif role == "Forum Moderators":
            self.listItem = self.driver.find_element(By.XPATH, self.custroledrp_listitem_forummoderators)
        elif role == "Vendors":
            self.listItem = self.driver.find_element(By.XPATH, self.custroledrp_listitem_vendors)
        else:
            self.listItem = self.driver.find_element(By.XPATH, self.custroledrp_listitem_guests)
        time.sleep(2)
        self.driver.execute_script("arguments [0].click()", self.listItem)  # if click method is not working, use this javascript
        time.sleep(2)
    def setManagerofVendor(self, visibleText):
        drp = Select(self.driver.find_element(By.XPATH, self.dropdown_managerofvendor_XPATH))
        drp.select_by_visible_text(visibleText)
    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, self.radiobtn_gender_male).click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH, self.radiobtn_gender_female).click()
        else:
            self.driver.find_element(By.XPATH, self.radiobtn_gender_male).click()
    def setFirstName(self, fName):
        self.driver.find_element(By.XPATH, self.textbox_firstname_XPATH).send_keys(fName)
    def setLastName(self, lName):
        self.driver.find_element(By.XPATH, self.textbox_lastname_XPATH).send_keys(lName)
    def setDOB(self, dob):
        self.driver.find_element(By.XPATH, self.textbox_date_of_birth).send_keys(dob)
    def setCompanyName(self,companyName):
        self.driver.find_element(By.XPATH, self.textbox_company_name).send_keys(companyName)
    def setAdminContent(self, adminContent):
        self.driver.find_element(By.XPATH, self.textbox_admin_comment_XPATH).send_keys(adminContent)
    def clickSave(self):
        self.driver.find_element(By.XPATH, self.btn_save_XPATH).click()
