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

print(driver.window_handles)
print(driver.current_window_handle)
print(driver.title)

"""3. Wiki-Search"""
"""3a. Enter a text in wiki search text box"""
wiki_search_box=driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
wiki_search_box.send_keys("Selenium")

"""3b. Click on search button"""
wikipedia_search_button=driver.find_element(By.CLASS_NAME, "wikipedia-search-button")
wikipedia_search_button.click()


"""4. Click on search option"""
try:
    wiki_search_result=driver.find_element(By.XPATH, '(//*[@id="wikipedia-search-result-link"]/a)[3]')
    wiki_search_result.click()
except:
    driver.refresh()
    wiki_search_box=driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
    wiki_search_box.send_keys("Selenium")
    wikipedia_search_button=driver.find_element(By.CLASS_NAME, "wikipedia-search-button")
    wikipedia_search_button.click()
    wiki_search_result=driver.find_element(By.XPATH, '(//*[@id="wikipedia-search-result-link"]/a)[3]')
    wiki_search_result.click()

print(driver.window_handles)
print(driver.current_window_handle)
list_of_windows=driver.window_handles

driver.switch_to.window(list_of_windows[1])
print(driver.title)

"""5. In new tab click on 'History' left menu item """
history_menu_item=driver.find_element(By.XPATH, '//*[@id="toc-History"]/a/div/span[2]')
history_menu_item.click()
print(history_menu_item.text)

driver.switch_to.alert.send_keys("Sowmya").accept()

"""https://demo.automationtesting.in/Frames.html"""
driver.switch_to.frame("singleframe")