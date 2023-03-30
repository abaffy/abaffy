# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

# Setting up the webdriver
driver = webdriver.Chrome()

#
# # Navigating to the Ebay.ca homepage
driver.get("https://www.ebay.ca")
time.sleep(3)

#
# # Finding the search bar and entering text
search_bar = driver.find_element("id", "gh-ac")
search_bar.send_keys("ip camera outdoor")

#
# # Submitting the search query
search_bar.send_keys(Keys.RETURN)

#
# # Waiting for the search results page to load
time.sleep(5)

#
# # Verifying that the search results page has loaded
assert "ip camera outdoor" in driver.title

#
# # Selecting a camera from the search results
camera_link = driver.find_element("xpath", "/html/body/div[8]/div[4]/div[2]/div[1]/div[2]/ul/li[2]/div/div[2]/a/div/span")
camera_link.click()

#
# # Waiting for the ip camera details page to load
time.sleep(5)

#
# # The camera details opens in a new window
# # store the original handle and switch to the new window
home_window = driver.window_handles
product_window = driver.window_handles[1]
driver.switch_to.window(product_window)

#
# # Verifying that the correct camera details page has loaded
assert "4K 8MP Turret Indoor/Outdoor Network PoE IP Camera Sony Image Sensor H.265" in driver.title

#
# # Adding the camera to the cart
add_to_cart_button = driver.find_element("link text", "Add to cart")
add_to_cart_button.click()

#
# # Waiting for the cart to update
time.sleep(5)

#
# # Verifying that the ip camera  has been added to the cart
cart_count = driver.find_element("xpath","/html/body/div[4]/header/div[1]/ul[2]/li[6]/div/a")
assert cart_count.text == "1"

#
# # Changing the quantity to 3 cameras
quantity_select = Select(driver.find_element("xpath", "/html/body/div[5]/div[2]/div/div[3]/div[1]/div/ul/li/div/div/div/div[1]/div/div[3]/div/div[1]/div[1]/div/span/span/select"))
quantity_select.select_by_value('3')

#
# # Waiting for the cart to update
time.sleep(5)

#
# # Verifying that the cart have been updated to 3 cameras
cart_count = driver.find_element("xpath","/html/body/div[4]/header/div[1]/ul[2]/li[6]/div/a")
assert cart_count.text == "3"

#
# # Check the language of the page is English
current_language = driver.find_element("partial link text", "Current language")
assert current_language.text == "English"

#
# # Closing all the windows of the webdriver
driver.quit()
