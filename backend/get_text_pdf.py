import fitz  # PyMuPDF

def get_clean_text_from_pdf(pdf_path):
    # Open the PDF file
    document = fitz.open(pdf_path)
    text = ""
    uri = "'https://web.archive.org/web/20240117233627/https://www.theatlantic.com/podcasts/archive/2023/08/are-ai-relationships-real/674965/'"
    # Extract the title if available
    title = document.metadata.get('title', 'Unknown Title')
    text += f"Title: {title}\n\n"
    text += f"Source: {uri}\n\n"
    
    # Iterate through each page
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    
    return text.strip()

# if __name__ == "__main__":
#     pdf_path = "test.pdf"
#     clean_text = get_clean_text_from_pdf(pdf_path)
#     print(clean_text)
