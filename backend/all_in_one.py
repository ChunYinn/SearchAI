import os
from url_to_pdf import print_to_pdf
from get_text_pdf import get_clean_text_from_pdf
from summarize_ai import summarize_text, count_tokens, calculate_price
from to_csv import extract_and_write_to_csv
from dotenv import load_dotenv
from openai import OpenAI

def main():
    load_dotenv()

    # Retrieve OpenAI API key from environment variables
    api_key = os.getenv("OPENAI_API_KEY")

    # Create an OpenAI client
    client = OpenAI(api_key=api_key)
    
    url = 'https://web.archive.org/web/20240117233627/https://www.theatlantic.com/podcasts/archive/2023/08/are-ai-relationships-real/674965/'  # Replace with your desired URL
    output_pdf_path = 'test.pdf'
    output_csv_path = 'output.csv'
    doc_id = 0

    # Step 1: Create PDF from URL
    try:
        print_to_pdf(url, output_pdf_path)
        print("Step 1: PDF creation completed successfully.")
    except Exception as e:
        print(f"Error in Step 1: {e}")
        return

    # Step 2: Extract text from PDF
    try:
        clean_text = get_clean_text_from_pdf(output_pdf_path, url)
        print("Step 2: Text extraction completed successfully.")
    except Exception as e:
        print(f"Error in Step 2: {e}")
        return

    # Step 3: Summarize the text
    try:
        summary = summarize_text(clean_text)
        print("Step 3: Text summarization completed successfully.")
    except Exception as e:
        print(f"Error in Step 3: {e}")
        return

    # Step 4: Write the summary to CSV
    try:
        extract_and_write_to_csv(summary, doc_id, url, output_csv_path)
        print("Step 4: CSV writing completed successfully.")
    except Exception as e:
        print(f"Error in Step 4: {e}")

if __name__ == "__main__":
    main()
