from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get("http://www.facebook.com")
login_email = browser.find_element_by_css_selector("input#email")
login_pwd = browser.find_element_by_css_selector("input#pass")
# login_email.send_keys("asdf@asdf.net")
# login_pwd.send_keys("bullshit")
log_in_button = browser.find_element_by_css_selector("input#u_0_2")
# log_in_button.click()
time.sleep(15)

# assert =
time.sleep(5)
browser.quit()
