from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Set up the webdriver
capabilities = DesiredCapabilities.IPHONE
driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)

# Open the app
driver.find_element_by_name('Your App Name').click()

# Get the battery percentage
battery_percentage = driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="Battery Level"]').text

# Print the battery percentage
print(battery_percentage)

# Close the app
driver.quit()