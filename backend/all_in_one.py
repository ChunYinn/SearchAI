import os
from url_to_pdf import print_to_pdf
from get_text_pdf import get_clean_text_from_pdf
from summarize_ai import summarize_text, count_tokens, calculate_price
from to_csv import extract_and_write_to_csv
from dotenv import load_dotenv
from openai import OpenAI

def main(urls):
    load_dotenv()

    # Retrieve OpenAI API key from environment variables
    api_key = os.getenv("OPENAI_API_KEY")

    # Create an OpenAI client
    client = OpenAI(api_key=api_key)
    
    output_pdf_path = 'temp.pdf'
    output_csv_path = 'output.csv'
    doc_id = 0

    # Ensure the output CSV file is empty before starting
    # with open(output_csv_path, 'w', newline='', encoding='utf-8') as file:
    #     pass

    for url in urls:
        # Increment document ID
        doc_id += 1

        # Step 1: Create PDF from URL
        try:
            print_to_pdf(url, output_pdf_path)
            print("Step 1: PDF creation completed successfully.")
        except Exception as e:
            print(f"Error in Step 1: {e}")
            continue

        # Step 2: Extract text from PDF
        try:
            clean_text = get_clean_text_from_pdf(output_pdf_path, url)
            print("Step 2: Text extraction completed successfully.")
        except Exception as e:
            print(f"Error in Step 2: {e}")
            continue

        # Step 3: Summarize the text
        try:
            summary = summarize_text(clean_text)
            print("Step 3: Text summarization completed successfully.")
        except Exception as e:
            print(f"Error in Step 3: {e}")
            continue

        # Step 4: Write the summary to CSV
        try:
            print(f"summary in step 4: \n{summary}")
            extract_and_write_to_csv(summary, doc_id, url, output_csv_path)
            print("Step 4: CSV writing completed successfully.")
        except Exception as e:
            print(f"Error in Step 4: {e}")

        # Remove the temporary PDF file
        if os.path.exists(output_pdf_path):
            os.remove(output_pdf_path)

if __name__ == "__main__":
    urls = [
        'https://web.archive.org/web/20240117233627/https://www.theatlantic.com/podcasts/archive/2023/08/are-ai-relationships-real/674965/',
        'https://link.springer.com/chapter/10.1007/978-981-16-6289-8_45',
        # Add more URLs here
    ]
    main(urls)
