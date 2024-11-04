import unittest
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

class TestOrangeHRMLogin(unittest.TestCase):


    def testLogin(self):
        options=ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("start-maximized")
        driver=Chrome(options=options)  
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.implicitly_wait(10)
        login_id_orangehrm = driver.find_element(By.NAME, "username")
        login_id_orangehrm.send_keys("Admin")

        login_pw_orangehrm = driver.find_element(By.NAME,"password")
        login_pw_orangehrm.send_keys("admin123")

        login_button = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
        login_button.click()
        
        expected_url="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index123"
        actual_url = driver.current_url
        
        self.assertEqual(actual_url, expected_url, "Login failed")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()