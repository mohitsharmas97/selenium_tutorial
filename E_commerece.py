from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

sleep(2)

# Add product
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

sleep(2)

# Open cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

sleep(2)

# Checkout
driver.find_element(By.ID, "checkout").click()

sleep(2)

# Customer details
driver.find_element(By.ID, "first-name").send_keys("Mohit")
driver.find_element(By.ID, "last-name").send_keys("Sharma")
driver.find_element(By.ID, "postal-code").send_keys("302001")

# Continue
driver.find_element(By.ID, "continue").click()

sleep(2)

# Finish order
driver.find_element(By.ID, "finish").click()

sleep(2)
message = driver.find_element(By.CLASS_NAME, "complete-header").text

assert message == "Thank you for your order!"

print("TEST PASSED")

# print("Order placed successfully")

driver.quit()