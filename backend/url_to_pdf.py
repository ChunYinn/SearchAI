import time
import base64
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

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
        
        # Wait for the page to load completely with a random delay (micmmicing human behavior)
        time.sleep(random.uniform(2, 5))

        # Print the page to PDF
        pdf = driver.execute_cdp_cmd("Page.printToPDF", {"printBackground": True})
        pdf_data = base64.b64decode(pdf["data"])

        ##i want beefore it being write to pdf, use ai todo the summary of the passage and add o nthe top, soi have to allow ai to read the content which need the readable part, or it dont have to be readable?

        #for readable in testing
        # readable_text = pdf_data.decode('latin1')  # Decoding binary data to text (non-printable characters included)
        # print("PDF data (decoded): ")
        # print(readable_text)

        # Save the PDF to a file
        with open(output_pdf_path, "wb") as f:
            f.write(pdf_data)
        
        print(f"PDF saved to {output_pdf_path}")

    finally:
        driver.quit()

if __name__ == "__main__":
    url = 'https://www.nejm.org/doi/full/10.1056/NEJMoa1411587'  # Replace with your desired URL
    output_pdf_path = 'test3.pdf'
    print_to_pdf(url, output_pdf_path)
