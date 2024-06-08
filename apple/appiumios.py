from appium import webdriver
import time

# Desired capabilities
desired_capabilities = {
    "platformName": "iOS",
    "platformVersion": "14.2",
    "deviceName": "iPhone 12",
    "automationName": "XCUITest",
    "app": "/path/to/your/app.ipa"
}

# Initialize the driver
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

# Wait for the app to launch
time.sleep(5)

# Find an element by accessibility ID
element = driver.find_element_by_accessibility_id("your_element_id")

# Click on the element
element.click()

# Wait for a new element to appear
new_element = driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='New Element']")

# Assert the new element is visible
assert new_element.is_displayed()

# Close the app
driver.quit()