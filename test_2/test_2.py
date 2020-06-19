import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait


class TestParallel2(unittest.TestCase):
    def setUp(self):
        capabilities = DesiredCapabilities.FIREFOX
        # capabilities['marionette'] = True

        
        # capabilities = DesiredCapabilities.FIREFOX
        self.driver = webdriver.Remote(
            command_executor="http://hub:4444/wd/hub",
            desired_capabilities=capabilities )
        delay=30
        myElem = WebDriverWait(self.driver,delay)
        # self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_three(self):
        driver = self.driver
        self.driver.implicitly_wait(30)
        driver.get("https://www.twitter.com")
        # driver.implicitly_wait(5)
    def test_one(self):
        driver = self.driver
        self.driver.implicitly_wait(30)
        driver.get("https://www.yahoo.com")
        # driver.implicitly_wait(5)
        print("test_one passed--------------------------------------")    

    def test_four(self):
        driver = self.driver
        self.driver.implicitly_wait(30)
        driver.get("https://www.facebook.com")
        # driver.implicitly_wait(5)
        
   
    def test_two(self):
        driver = self.driver
        self.driver.implicitly_wait(30)
        driver.get("https://www.youtube.com")
        # driver.implicitly_wait(5)


    def tearDown(self):
        self.driver.quit()
# 
       

if __name__ == "__main__":
    unittest.main()