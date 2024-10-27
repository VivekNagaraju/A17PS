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

"""3. Fetch data from the static web table"""
cell21=driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[5]/td[2]')
print(cell21.text)