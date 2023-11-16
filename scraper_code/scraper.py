import utils, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=chrome_options)

questions_data = []
page_counter = 1

# get the page loaded, and select necessary buttons/options
utils.setup_home_page(driver, page_counter)

while True:
    print("page_number: ", page_counter)

    # Find all rows in the table
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@role='rowgroup']/div"))
    )

    rows = driver.find_elements(By.XPATH, "//div[@role='rowgroup']/div")

    for row in rows:

        question_title, question_link, question_categories, question_difficulty = utils.find_question_details(row)
        print(question_title)
        # solution = utils.find_solution(driver, row)
        question_description = utils.question_description(question_link, driver)
        
        if (question_description == "Premium Question! Subscribe to us to view this question!"):
            print(" -- Premium Question...will not have detailed description")
        
        # Save data in JSON format
        question_data = {
            "id": len(questions_data),
            "title": question_title,
            "difficulty": question_difficulty,
            "categories": question_categories,
            "description": question_description,
            "question_link": question_link,
            "solution_link": question_link + "/solutions",
        }
        
        questions_data.append(question_data)

        # Close the current tab and switch back to the main tab
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    utils.add_data_to_file(questions_data, page_counter)

    # clear data array
    questions_data.clear()

    # Check if there is a next page, move to next page if there is
    next_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='next']")
    if not next_button:
        break

    # Go to the next page
    next_button.click()
    page_counter += 1
    time.sleep(3) # forced wait for next bunch of questions to load

# # Close the browser
# driver.quit()
