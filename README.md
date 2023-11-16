# LeetCode Questions Scraper

This repository contains a Python-based LeetCode questions scraper, designed to extract and organize data from the LeetCode platform. The code is structured into several modules, each serving a specific purpose.

## Code Structure

- **scraper_code/**: Contains the core scraping modules.
  - **scraper.py**: Primary script for scraping LeetCode questions.
  - **scrape_code.py**: Additional script for extracting code snippets from questions.

- **utils.py**: A collection of utility functions used in the scraping process.

- **combiner.py**: Combines the processed data into a consolidated JSON file.

## How to Use

1. **Scraper Execution:**

   Start with the main scraping script:

   ```bash
   cd scraper_code
   python scraper.py
   ```

   This will generate JSON files in the `scraped_data` directory.

2. **Chromedriver Configuration:**

   Open the `scraper.py` file in the `scraper_code` directory and specify the path to the ChromeDriver executable in the code. Replace `'path/to/chromedriver.exe'` with the actual path on your system.

   ```python
   # Specify the path to ChromeDriver executable
   chrome_driver_path = 'path/to/chromedriver.exe'  # Replace with the actual path

   # Initialize the WebDriver
   chrome_options = webdriver.ChromeOptions()
   chrome_options.add_argument("--start-maximized")
   chrome_options.add_argument("--disable-notifications")
   driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
   ```

3. **Combining Data:**

   Combine all the scraped data:

   ```bash
   python combiner.py
   ```

   The consolidated JSON file will be generated and can be found in the root directory.

## Collaboration

Collaboration and contributions are welcome! If you have ideas for improvements, additional features, or optimizations, feel free to fork the repository, make your changes, and submit a pull request. Let's work together to enhance this LeetCode questions scraper!

Happy coding! 🚀