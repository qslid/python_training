# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class group_add(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    
    def test_group_add(self):
        success = True
        wd = self.wd
        wd.get("http://autotest.h1n.ru/addressbook/group.php")
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
    #   wd.find_element_by_xpath("//div[3]/div[2]/div[1]/div[1]/div[2]/button[1]").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("NAME")
     #   if not wd.find_element_by_xpath("//div[@id='content']//select[normalize-space(.)='[none] Group']//option[1]").is_selected():
  #          wd.find_element_by_xpath("//div[@id='content']//select[normalize-space(.)='[none] Group']//option[1]").click()
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("HEADER")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("FOOTER")
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("group page").click()
        wd.find_element_by_link_text("Logout").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
