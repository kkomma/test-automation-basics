from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome("/Users/veeranica/Downloads/chromedriver")
browser.get("http://www.google.com")
browser.find_element(By.NAME, 'q').send_keys("Sachin Tendulkar")
browser.find_element(By.NAME, 'q').send_keys(Keys.ENTER)
wait = WebDriverWait(browser, 2)
page_title = browser.title
assert page_title == "Sachin Tendulkar - Google Search"
text='Sachin Ramesh Tendulkar is an Indian former international cricketer who captained the Indian national team.'
assert text in browser.page_source
browser.quit()