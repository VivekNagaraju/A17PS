from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

"""1. Launch chrome browser"""
options=ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver=Chrome(options=options)

"""2. Navigate to Practice Site"""
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)

"""3. Upload file"""
single_file_input = driver.find_element(By.ID, 'singleFileInput')
single_file_input.send_keys("C:/Users/admin/Desktop/hello vivek.txt")

driver.save_screenshot("C:/Users/admin/Desktop/ss.png")