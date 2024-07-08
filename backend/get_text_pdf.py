import slate3k as slate

def get_clean_text_from_pdf(pdf_path):
    text_content = ""
    with open(pdf_path, 'rb') as pdf_file:
        # Use slate to extract text from the PDF
        extracted_text = slate.PDF(pdf_file)
        # Join the list of strings into a single string with newlines between pages
        text_content = "\n".join(extracted_text)
    
    # Remove extra whitespace and line breaks
    text_content = " ".join(text_content.split())
    return text_content
