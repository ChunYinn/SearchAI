import pdfplumber
import re

def get_clean_text_from_pdf(pdf_path):
    text_content = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            # Extract the entire page text, including headers and footers
            text_content += page.extract_text() + "\n"
    
    # Define patterns to remove unwanted sections
    patterns_to_remove = [
        r'ADVERTISEMENT', 
        r'THIS SITE USES COOKIES.*?Cookie Information page\.',  # Non-greedy match for cookie notices
        r'\f',  # Page breaks
        r'Learn more about.*?Cookie Information page\.',  # Another pattern for cookie notices
        r'Published January .*? DOI: .*? VOL\.',  # Publication details
        r'\(Funded by the Dutch.*?Current Controlled Trials number, ISRCTN.*?\)\.',  # Specific trial info
    ]

    # Remove unwanted sections
    for pattern in patterns_to_remove:
        text_content = re.sub(pattern, '', text_content, flags=re.DOTALL)

    # Remove extra whitespace and line breaks
    text_content = re.sub(r'\s+', ' ', text_content)
    text_content = text_content.strip()

    return text_content

print(get_clean_text_from_pdf('test3.pdf'))
