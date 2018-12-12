from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://techstepacademy.com/trial-of-the-stones")
# riddle of stones
stone_input = browser.find_element_by_id('r1Input')
stone_answer_button = browser.find_element_by_css_selector("button#r1Btn")
stone_result = browser.find_element_by_css_selector("div#passwordBanner > h4")
# riddle of secrets
secrets_input = browser.find_element_by_css_selector("input#r2Input")
secrets_answer_button = browser.find_element_by_css_selector("button#r2Butn")
# two merchants
# simple method, looking for the name
richest_merchant_name = browser.find_element_by_xpath("//p[text()='3000']/../span").text
merchant_input = browser.find_element_by_id('r3Input')
merchant_answer_button = browser.find_element_by_css_selector("button#r3Butn")

check_button = browser.find_element_by_css_selector("button[name='checkButn']")

complete_message = browser.find_element_by_css_selector("div#trialCompleteBanner h4")

# run script
stone_input.send_keys('rock')
stone_answer_button.click()
password = stone_result.text

secrets_input.send_keys(password)
secrets_answer_button.click()

merchant_input.send_keys(richest_merchant_name)
merchant_answer_button.click()

check_button.click()
assert complete_message.text == "Trial Complete"

browser.quit()
