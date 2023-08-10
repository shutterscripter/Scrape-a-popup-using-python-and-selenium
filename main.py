from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up Chrome WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Load the website
    driver.get('https://www.geeksforgeeks.org/')
    time.sleep(3)

    # Click on the element
    driver.find_element(By.XPATH, '//*[@id="userProfileId"]').click()
    print("Clicked on Element!")
    time.sleep(5)

    # Update the email and password
    email = driver.find_element(By.XPATH, '//*[@id="luser"]')
    passwd = driver.find_element(By.XPATH, '//*[@id="password"]')
    time.sleep(3)

    email.clear()
    email.send_keys('classes@geeksforgeeks.org')
    time.sleep(2)

    passwd.clear()
    passwd.send_keys('geeksforgeeks')
    time.sleep(3)

    print("Info changed successfully")

except Exception as ex:
    print(ex)

finally:
    # Close the browser
    driver.quit()
