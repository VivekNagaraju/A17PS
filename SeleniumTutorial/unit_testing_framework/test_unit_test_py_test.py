from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.parametrize("username, password, expected_url",
                         [
                             ("Admin", "admin123", "dashboard/index"),
                             ("Admin", "admin", "auth/login")
                             ]
    )


def test_Login(username, password, expected_url):
        options=ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("start-maximized")
        driver=Chrome(options=options)  
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.implicitly_wait(10)
        login_id_orangehrm = driver.find_element(By.NAME, "username")
        login_id_orangehrm.send_keys(username)

        login_pw_orangehrm = driver.find_element(By.NAME,"password")
        login_pw_orangehrm.send_keys(password)

        login_button = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
        login_button.click()
        
        # expected_url="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index123"
        actual_url = driver.current_url
        
        # self.assertEqual(actual_url, expected_url, "Login failed")
        
        # assert actual_url == expected_url, "Login Failed"
        
        assert expected_url in actual_url, "Login Failed"