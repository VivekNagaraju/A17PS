from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

"""1. Launch chrome browser"""
options=ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver=Chrome(options=options)

"""2. Navigate to Practice Site"""
driver.get("https://testautomationpractice.blogspot.com/")

"""3. Wiki-Search"""
"""3a. Enter a text in wiki search text box"""
wiki_search_box=driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
wiki_search_box.send_keys("Selenium")

"""3b. Click on search button"""
wikipedia_search_button=driver.find_element(By.CLASS_NAME, "wikipedia-search-button")
wikipedia_search_button.click()

"""4. Click on search option"""
driver.find_element(By.XPATH, "(//*[@id='wikipedia-search-result-link']/a)[3]")
