import time
import base64
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def accept_cookies(driver):
    try:
        # Try to find the accept button by its ID
        accept_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "truste-consent-button"))
        )
        accept_button.click()
        print("Cookies accepted")
    except Exception as e:
        print("No cookie consent dialog found or there was an issue:", str(e))

def print_to_pdf(url, output_pdf_path):
    # Set up Chrome options to enable printing to PDF
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode
    chrome_options.add_argument('--disable-gpu')
    
    # Set a realistic User-Agent string
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

    # Set up Chrome WebDriver service
    service = Service()

    # Initialize WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Navigate to the URL
        driver.get(url)
        
        # Wait for the page to load completely with a random delay (mimicking human behavior)
        time.sleep(random.uniform(2, 5))
        
        # Accept cookies
        accept_cookies(driver)
        
        # Wait for a bit to ensure the page is ready after accepting cookies
        time.sleep(random.uniform(2, 5))

        # Print the page to PDF
        pdf = driver.execute_cdp_cmd("Page.printToPDF", {"printBackground": True})
        pdf_data = base64.b64decode(pdf["data"])

        # Save the PDF to a file
        with open(output_pdf_path, "wb") as f:
            f.write(pdf_data)
        
        print(f"PDF saved to {output_pdf_path}")

    finally:
        driver.quit()

# if __name__ == "__main__":
#     url = 'https://web.archive.org/web/20240117233627/https://www.theatlantic.com/podcasts/archive/2023/08/are-ai-relationships-real/674965/'  # Replace with your desired URL
#     output_pdf_path = 'test.pdf'
#     print_to_pdf(url, output_pdf_path)
