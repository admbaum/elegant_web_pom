from selenium import webdriver

from pages.training_ground_page import TrainingGroundPage

# test setup
browser = webdriver.Chrome()
test_value = 'it worked'

# test
trng_page = TrainingGroundPage(driver=browser)
trng_page.go()
assert trng_page.button1.text == 'Button1'
browser.quit()
