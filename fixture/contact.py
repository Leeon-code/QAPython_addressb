from selenium.webdriver.common.by import By

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def create_contact(self, contact):
        wd = self.app.wd
        # init group creation
        self.open_add_contact_page()

        # fill contact form
        wd.find_element(By.NAME, "firstname").send_keys("%s" % contact.firstname) #("wqeqwe")
        wd.find_element(By.NAME, "middlename").send_keys("%s" % contact.middlename) #("qwe")
        wd.find_element(By.NAME, "lastname").send_keys("%s" % contact.lastname) #("wqe")
        wd.find_element(By.NAME, "nickname").send_keys("%s" % contact.nickname) #("qwee")
        wd.find_element(By.NAME, "title").send_keys("%s" % contact.title) #("qweqw")
        wd.find_element(By.NAME, "company").send_keys("%s" % contact.company) #("qweqwe")
        wd.find_element(By.NAME, "address").send_keys("%s" % contact.address) #("qwewe")
        wd.find_element(By.NAME, "mobile").send_keys("%s" % contact.mobile) #("872364823")
        wd.find_element(By.NAME, "email").send_keys("%s" % contact.email) #("qweqw@wqewqe.ru")

        # submit contact creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        # select first contact
        wd.find_element(By.NAME, "selected[]").click()
        # submit deletion
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        self.open_home_page()

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home").click()
