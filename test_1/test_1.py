import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestParallel1(unittest.TestCase):
    def setUp(self):
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        # capabilities['marionette'] = True
       
        

        capabilities = DesiredCapabilities.CHROME
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True
        capabilities['javascriptEnabled']=True

        self.driver = webdriver.Remote(
            command_executor="http://hub:4444/wd/hub",
            desired_capabilities=capabilities,options=chrome_options )

        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        # driver.implicitly_wait(5)
    def test_six(self):
        driver = self.driver
        self.driver.implicitly_wait(10)
        driver.get("https://www.twitter.com")
        # driver.implicitly_wait(5)
    def test_seven(self):
        driver = self.driver
        self.driver.implicitly_wait(10)
        driver.get("https://www.yahoo.com")
        print("test_one passed--------------------------------------")
    def test_eight(self):
        driver = self.driver
        self.driver.implicitly_wait(10)
        driver.get("https://www.facebook.com")
        # driver.implicitly_wait(5)
        
   
    def test_nine(self):
        driver = self.driver
        self.driver.implicitly_wait(10)
        driver.get("https://www.youtube.com")
        # driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()