from selenium import selenium
import unittest, time, re
import seleniumtest

class NewTest(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://ec2-54-235-205-104.compute-1.amazonaws.com/")
        self.selenium.start()
    
    def test_new(self):
        sel = self.selenium
        sel.open("/4350app/default/logout")
        # Login
        sel.click("link=Login")
        sel.wait_for_page_to_load("30000")
        sel.click("t2_student_number")
        sel.type("t2_password", "")
        sel.click("//input[@value='Login']")
        sel.wait_for_page_to_load("30000")
        try: self.failUnless(sel.is_text_present("You have successfully logged in"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        # Logout
        sel.open("/4350app/default/login")
        sel.click("link=Logout")
        sel.wait_for_page_to_load("30000")
        try: self.failUnless(sel.is_text_present("Logged Out"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        # Login
        sel.open("/4350app/default/logout")
        sel.click("t2_student_number")
        sel.type("t2_password", "")
        sel.click("//input[@value='logout']")
        sel.wait_for_page_to_load("30000")
        try: self.failUnless(sel.is_text_present("Logged In"))
        except AssertionError, e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    #unittest.main()
    seleniumtest.runInSeleniumRC(unittest.main)() 
