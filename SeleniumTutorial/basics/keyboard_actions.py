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

'''3. Create ActionChains class object'''
my_actions=ActionChains(driver)

"""
'''4. Copying the text from Field1 text box using Keyboard shortcuts'''
field1=driver.find_element(By.ID, 'field1')
field2=driver.find_element(By.ID, 'field2')
my_actions.click(field1).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)
my_actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL)
my_actions.click(field2).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL)
my_actions.perform()

'''5. Pasting the text into Field2 text box using Keyboard shortcuts'''
field2=driver.find_element(By.ID, 'field2')
my_actions.key_down(Keys.CONTROL, field2).send_keys('v').key_up(Keys.CONTROL).perform()
"""

'''4. Copy paste without using ActionChains class Object'''
field1=driver.find_element(By.ID, 'field1')
field2=driver.find_element(By.ID, 'field2')
field1.send_keys(Keys.CONTROL, 'a')
field1.send_keys(Keys.CONTROL, 'c')
field2.send_keys(Keys.CONTROL, 'v')