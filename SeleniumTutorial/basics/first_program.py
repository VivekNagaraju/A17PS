'''
Created on 15-Oct-2024

@author: admin
'''
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

"""1. Launch chrome browser"""
options=ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver=Chrome(options=options)

"""2. Navigate to Practice Site"""
driver.get("https://testautomationpractice.blogspot.com/")

"""3. Enter name"""
"""3a. Locate the element"""
name_txtbx=driver.find_element(By.ID, "name")

"""3b. Interact with the element"""
name_txtbx.send_keys("Vivek")
