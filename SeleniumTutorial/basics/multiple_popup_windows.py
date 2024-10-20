from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

"""1. Launch chrome browser"""

options=ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver=Chrome(options=options)

"""2. Navigate to Practice Site"""
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)

"""3. Click on PopUp windows"""
popup_windows_btn = driver.find_element(By.ID, "PopUp")
popup_windows_btn.click()

print(driver.window_handles)

