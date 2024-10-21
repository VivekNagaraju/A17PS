from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

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

'''4. Double-click on an element'''
copy_text_btn = driver.find_element(By.XPATH, '//button[@ondblclick="myFunction1()"]')
my_actions.double_click(copy_text_btn).perform()


'''6. Drag and drop'''
source=driver.find_element(By.ID, 'draggable')
target=driver.find_element(By.ID, 'droppable')
my_actions.drag_and_drop(source, target).perform()