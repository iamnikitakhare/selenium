from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set the path to your web driver executable. Download the appropriate driver for your browser.
driver_path = 'path_to_your_webdriver_executable'

# Initialize the webdriver (e.g., for Chrome)
driver = webdriver.Chrome(executable_path=driver_path)

# Open the web application
driver.get('http://your-sample-website.com')

# Find the username and password input fields and the login button
username_input = driver.find_element_by_id('username')
password_input = driver.find_element_by_id('password')
login_button = driver.find_element_by_id('login-button')

# Enter your login credentials
username_input.send_keys('your_username')
password_input.send_keys('your_password')

# Click the login button
login_button.click()

# Add a brief sleep to allow the page to load (you might need to adjust the time)
time.sleep(2)

# Verify if the login was successful (you can check for elements on the next page)
if 'Welcome' in driver.page_source:
    print('Login successful!')
else:
    print('Login failed!')

# Close the browser window
driver.quit()
