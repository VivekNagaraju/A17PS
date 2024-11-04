from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

"""1. Launch chrome browser"""
options=ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver=Chrome(options=options)

"""2. Navigate to Practice Site"""
driver.get("https://www.amazon.in/s?k=mobile&rh=n%3A1389401031&ref=nb_sb_noss")
driver.implicitly_wait(10)

"""3. Scroll to price range slider"""
my_actions = ActionChains(driver)
my_actions.scroll_by_amount(0, 300).perform()
print("Scrolled")
time.sleep(10)

"""4. Set price range"""
lower_bound_slider = driver.find_element(By.ID, 'p_36/range-slider_slider-item_lower-bound-slider')
# my_actions.click_and_hold(lower_bound_slider).move_by_offset(50, 0).release().perform()
# my_actions.drag_and_drop_by_offset(lower_bound_slider, 70, 0).perform()
print(lower_bound_slider.get_dom_attribute("aria-valuetext"))
print(lower_bound_slider.get_property("aria-valuetext"))
# print("Dragged")
# time.sleep(10)
# lower_bound_slider.send_keys("100")
# print("Entered slider value")
# lower_bound_slider.submit()
# time.sleep(10)
# go_button = driver.find_element(By.ID, 'a-autoid-31')
# go_button.click()
# print("clicked on Go")

# document.getElementById("p_36/range-slider_slider-item_lower-bound-slider").value=500
# document.getElementById("p_36/range-slider_slider-item_lower-bound-slider").dispatchEvent(new Event("change"))

expected_url="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
actual_url = driver.current_url

# if actual_url == expected_url:
#     print("Test passed")
# else:
#     print("Test Failed")
    
assert actual_url == expected_url