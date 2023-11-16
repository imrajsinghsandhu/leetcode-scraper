import os, json, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=chrome_options)

with open('../first_hundred_questions.json', 'r') as f:
    data = json.load(f)

for question in data:
    # open the webpage, using chromedriver and selenium
    driver.get(question['question_link'])
    time.sleep(100000)

    # Let the code segment come into full loaded state
    code_segment_xpath = "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[11]/div/div[2]/div[1]/div/div/div[1]/div[2]/div[1]/div[4]"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, code_segment_xpath))
    )

    code_segment = driver.find_element(By.XPATH, code_segment_xpath)
    print(code_segment)

    # add code element to question
    question['code'] = code_segment