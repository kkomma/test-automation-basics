import pyautogui

# Move the mouse to the top-left corner of the screen
pyautogui.moveTo(0, 0)

# Click the mouse button
pyautogui.click()

# Type a message
pyautogui.typewrite("Hello, world!")

# Press the Enter key
pyautogui.press("enter")
# Wait for 2 seconds
pyautogui.sleep(20)

# Open the Settings app on iPhone
# pyautogui.press("home")  # Press the home button to go to the home screen
# pyautogui.swipe(100, 500, 100, 100, duration=0.5)  # Swipe up to reveal the Control Center
# pyautogui.click(200, 600)  # Click on the Control Center's settings icon