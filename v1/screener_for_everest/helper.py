from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_sfe_data():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)  # Or use webdriver.Firefox(options=options) if using Firefox

    url = "https://chartink.com/screener/copy-10-years-high-and-supertrend-7"
    driver.get(url)

    # Initialize list to collect all rows
    all_rows = []

    try:
        while True:
            # Wait for the table to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "DataTables_Table_0"))
            )

            # Get page source and parse it with BeautifulSoup
            soup = BeautifulSoup(driver.page_source, "html.parser")

            # Find the table and extract rows
            table = soup.find("table", {"id": "DataTables_Table_0"})
            
            # Extract headers only on the first page
            if not all_rows:
                headers = [header.text.strip() for header in table.find_all("th")]

            # Extract table rows
            rows = []
            for row in table.find("tbody").find_all("tr"):
                cells = row.find_all("td")
                row_data = [cell.text.strip() for cell in cells]
                rows.append(row_data)

            # Add current page rows to all_rows
            all_rows.extend(rows)

            # Check if "Next" button is enabled
            next_button = driver.find_element(By.ID, "DataTables_Table_0_next")
            if "disabled" in next_button.get_attribute("class"):
                break  # Exit loop if "Next" button is disabled

            # Click on the "Next" button
            next_button.click()
            time.sleep(2)  # Add a short delay to wait for the next page to load

    finally:
        # Close the WebDriver
        driver.quit()

    # Convert all rows to a DataFrame
    df = pd.DataFrame(all_rows, columns=headers)

    return df