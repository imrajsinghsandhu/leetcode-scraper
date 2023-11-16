import os, json, time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException

def setup_home_page(driver, page_number):
    # Navigate to LeetCode
    driver.get("https://leetcode.com/problemset/all/?page={}".format(page_number))

    # Close first pop up
    pop_up_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/section/footer/button[1]"))
    )

    pop_up_button.click()

    # Wait for the button to be clickable
    show_categories_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div[1]/div[5]/div[1]/div/div[5]/div[2]/button"))
    )
    
    # Click the button
    show_categories_button.click()

    # Wait for the option to be clickable
    option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div[1]/div[5]/div[1]/div/div[5]/div[2]/div/div[1]/div/span[1]"))
    )

    # Select the option
    option.click()
    show_categories_button.click()

    # num_qns_per_page_button = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div[1]/div[5]/div[3]/div/button"))
    # )

    # num_qns_per_page_button.click()

    # select_option = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div[1]/div[5]/div[3]/div/ul/li[3]"))
    # )

    # select_option.click()

def find_solution(row):
    solution = ""
    try:
        solution = row.find_element(By.XPATH, ".//div[3]/a")
        if (solution is not ""):
            solution_link = solution.get_attribute('href')
            return solution_link
    except Exception:
        return solution
    
    return solution

def find_question_details(row):
        # Normal question
        # find the link to the question, categories, and difficulty in this section
        
        question_title = row.find_element(By.XPATH, ".//div[2]/div/div/div/div/a").text.strip()
        question_link = row.find_element(By.XPATH, ".//div[2]/div/div/div/div/a").get_attribute("href")
        # Split the question name by the period and remove the numbering
        question_title_only = ' '.join(question_title.split('.')[1:]).strip()
        try:
            question_categories = row.find_element(By.XPATH, ".//div[2]/div/div/div[2]").text.strip()
        except NoSuchElementException:
            time.sleep(2)
           
        try:
            question_categories = row.find_element(By.XPATH, ".//div[2]/div/div/div[2]").text.strip()
        except NoSuchElementException:
            question_categories = "no categories\n"

        question_categories_com_sep = question_categories.split("\n")
        question_difficulty = row.find_element(By.XPATH, ".//div[5]").text

        return [question_title_only, question_link, question_categories_com_sep, question_difficulty]

def question_description(question_link, driver):
        # get question description
        # Open a new tab/window
        driver.execute_script("window.open('about:blank', '_blank');")

        # Switch to the new tab
        driver.switch_to.window(driver.window_handles[-1])

        # Navigate to the question link (URL)
        driver.get(question_link)

        # Find the element with the specified class and attribute
        try:
            element = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div.xFUwe[data-track-load="description_content"]'))
            )
        except TimeoutException:
            return "Premium Question! Subscribe to us to view this question!"

        try:
            # Get the inner HTML content of the element
            question_description = element.get_attribute("innerHTML")
            return question_description
        except StaleElementReferenceException:
            pass

        try:
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div.xFUwe[data-track-load="description_content"]'))
            )
        except TimeoutException:
            return "Premium Question! Subscribe to us to view this question!"

        return element.getAttribute("innerHTML")
                  
def add_data_to_file(questions_data, page_counter):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_directory = os.path.join(base_dir, "scraped_data")

    # Define the filename for the JSON file with the page counter as part of the name
    json_filename = os.path.join(output_directory, f'leetcode_questions_page_{page_counter}.json')
    
    # Save the collected data to a JSON file first, before moving on to the next page
    with open(json_filename, 'w', encoding='utf-8') as json_file:
        json.dump(questions_data, json_file, ensure_ascii=False, indent=4)