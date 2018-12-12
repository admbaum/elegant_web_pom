from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present
import time

browser = webdriver.Chrome()
browser.get("http://techstepacademy.com/training-ground")
# time.sleep(3)
# print("I have arrived")
# WebDriverWait(browser, 10).until(alert_is_present())
# print("an alert appeared")
# browser.quit()
sel = browser.find_element_by_id('sell')
my_select = Select(sel)

