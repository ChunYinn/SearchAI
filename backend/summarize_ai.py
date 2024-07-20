import os
import tiktoken
from dotenv import load_dotenv
from get_text_pdf import get_clean_text_from_pdf
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Create an OpenAI client
client = OpenAI(api_key=api_key)

def truncate_text_to_fit_token_limit(text, max_token_length):
    # Assume 4 characters per token as a rough average
    avg_characters_per_token = 4
    max_text_length = int(max_token_length * avg_characters_per_token)
    
    return text[:max_text_length]

def summarize_text(clean_text):
    # Define the prompt
    prompt_template = (
    """You are a good summarizer that summarizes the text. 
    Include the original title, author, publication year (as PubYear , year), publication date (as PubDate, month and date), source (based on the URL source of the text content), and category (like Reddit post, YouTube transcript, blog post, etc.) in the output. 
    If the title is unclear from the provided text, infer a suitable title based on the content. 
    If the author is not mentioned, label the author as "Unknown." 
    If the publication year or date is not mentioned, label them as "Unknown."
    For the source, extract the main domain from the URL (e.g., www.youtube.com should be labeled as "YouTube").
    Extract the year from the publication date to use as PubYear. 
    The output should be in the format: 
    {title: "", author: "", PubYear: "", PubDate: "", source: "", category: ""} 
    {summarized content: ""} 
    Summarize the following article by providing a summary paragraph, followed by key themes and quotes that explore the themes. 
    Here is the text to summarize:"""
)


    
    # Define the maximum token length for the entire context
    max_context_length = 16385
    
    # Calculate the length of the prompt template in tokens
    avg_characters_per_token = 4
    prompt_template_length_in_tokens = len(prompt_template) // avg_characters_per_token
    
    # Calculate the available length for the clean text
    max_token_length_for_clean_text = max_context_length - prompt_template_length_in_tokens - 1000  # reserving 1000 tokens for the summary
    
    # Truncate the clean text to fit within the available length
    clean_text = truncate_text_to_fit_token_limit(clean_text, max_token_length_for_clean_text)
    
    # Create the full prompt
    prompt = prompt_template + clean_text

    # Call OpenAI API to summarize the text
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="gpt-3.5-turbo",
        max_tokens=1000  # Limit the length of the summary
    )

    # Extract the summarized text from the response
    summarized_text = chat_completion.choices[0].message.content.strip()

    return summarized_text

def count_tokens(text):
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    tokens = encoding.encode(text)
    return len(tokens)

def calculate_price(token_count, model="gpt-3.5-turbo"):
    prices = {
        "gpt-3.5-turbo": {
            "input": 0.00050, 
            "output": 0.00150,
            "batch_input": 0.00025,
            "batch_output": 0.00075
        },
        "gpt-3.5-turbo-instruct": {
            "input": 0.00150, 
            "output": 0.00200,
            "batch_input": 0.00075,
            "batch_output": 0.00100
        }
    }
    
    input_tokens = token_count  # Assuming all tokens are input tokens for simplicity
    output_tokens = 1000  # Max tokens for summary
    
    if model in prices:
        input_price = prices[model]["input"] * input_tokens / 1000
        output_price = prices[model]["output"] * output_tokens / 1000
        total_price = input_price + output_price
        return total_price
    else:
        raise ValueError("Model pricing not available")

if __name__ == "__main__":
    # Extract clean text from PDF
    clean_text = get_clean_text_from_pdf('test.pdf')
    text_count = len(clean_text)
    token_count = count_tokens(clean_text)
    print(f"Text count: {text_count}")
    print(f"Token count: {token_count}")
    
    # Summarize the extracted text
    try:
        summary = summarize_text(clean_text)
        print(summary)
        
        # Calculate price
        price = calculate_price(token_count)
        # print(f"Estimated price: ${price:.5f}")
        
    except Exception as e:
        print(f"Error: {e}")
