from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
import time

"""1. Launch chrome browser"""


options=ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver=Chrome(options=options)

"""2. Navigate to Practice Site"""
driver.get("https://demo.automationtesting.in/Frames.html")
driver.implicitly_wait(10)

"""3. Type in text box inside iframe"""
"""3a. Switch to iframe"""
driver.switch_to.frame(0)
iframe_heading= driver.find_element(By.XPATH, '//h5')
print(iframe_heading.text)

"""3b. Type into text box"""
iframe_txtbx = driver.find_element(By.XPATH, '/html/body/section/div/div/div/input')
iframe_txtbx.send_keys("Vivek")

"""4. Click on 'Iframe within an Iframe' btn"""
# driver.find_element(By.XPATH, '/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a')
# (//a[@class="analystic"])[2]

driver.switch_to.parent_frame()

iframes_btn = driver.find_element(By.LINK_TEXT, 'Iframe with in an Iframe')
iframes_btn.click()

# outer_iframe=driver.find_element(By.XPATH, '(//iframe)[2]')
# driver.switch_to.frame(outer_iframe)
driver.switch_to.frame(1)
iframe_heading= driver.find_element(By.XPATH, '//h5')
print(iframe_heading.text)


# inner_iframe=driver.find_element(By.XPATH, '//iframe')
# driver.switch_to.frame(inner_iframe)
driver.switch_to.frame(0)
iframe_heading= driver.find_element(By.XPATH, '//h5')
print(iframe_heading.text)

# time.sleep(10)
txtbx_inner_iframe = driver.find_element(By.XPATH, '//input')
txtbx_inner_iframe.send_keys("Vivek")

