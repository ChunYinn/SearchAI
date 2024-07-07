import tiktoken
from get_text_pdf import get_clean_text_from_pdf

def count_tokens(text):
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    tokens = encoding.encode(text)
    return len(tokens)

clean_text = get_clean_text_from_pdf('test3.pdf')
token_count = count_tokens(clean_text)
print(f"Token count: {token_count}")
