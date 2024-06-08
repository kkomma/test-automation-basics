from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
# options.add_argument("--window-size=1920,1080")
# options.add_argument("--disable-extensions")
# options.add_argument("--disable-infobars")
# options.add_argument("--start-maximized")

browser = webdriver.Chrome(
    service=Service("/Users/veeranica/Downloads/driver/chromedriver"),
    options=options
    # ,keep_alive=True
)

browser.get("http://www.google.com")
browser.find_element(By.NAME, 'q').send_keys("Sachin Tendulkar")
browser.find_element(By.NAME, 'q').send_keys(Keys.ENTER)
wait = WebDriverWait(browser, 2)
page_title = browser.title
assert page_title == "Sachin Tendulkar - Google Search"
text='Sachin Ramesh Tendulkar'
assert text in browser.page_source
browser.quit()