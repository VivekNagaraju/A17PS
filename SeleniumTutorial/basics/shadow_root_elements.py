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

"""3. Enter text inside shadow root"""
script='document.querySelector("#shadow_host").shadowRoot.querySelector("input[type=text]:nth-child(5)").value=arguments[0]'
arg="Hello"
driver.execute_script(script, arg)

"""4. File upload inside shadow root"""
'''4a. Identifying the parent element'''
shadow_host=driver.find_element(By.ID, "shadow_host") 

'''4b. Getting access to shadowroot elements'''
shadow_root=driver.execute_script("return arguments[0].shadowRoot", shadow_host) # javascript: shadow_host.shadowRoot

'''4c. Locating and interacting with the elements inside shadowroot'''
file_input=shadow_root.find_element(By.CSS_SELECTOR, "input[type=file]:nth-child(9)")
file_input.send_keys("C:/Users/admin/Desktop/hello vivek.txt")