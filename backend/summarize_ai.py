import os
import tiktoken
import openai
from dotenv import load_dotenv
from get_text_pdf import get_clean_text_from_pdf

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

def truncate_text_to_fit_token_limit(text, max_token_length):
    # Assume 4 characters per token as a rough average
    avg_characters_per_token = 4
    max_text_length = int(max_token_length * avg_characters_per_token)
    
    return text[:max_text_length]

def summarize_text(clean_text):
    # Define the prompt
    prompt_template = (
        "You are a good summarizer that summarizes the text. "
        "Include the original title of the text inside the output. "
        "The output should be in the format: {title: \"\"} and {summarized content: \"\"}. "
        "Here is the text to summarize:\n\n"
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
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000  # Limit the length of the summary
    )

    # Extract the summarized text from the response
    summarized_text = response['choices'][0]['message']['content'].strip()

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
    clean_text = get_clean_text_from_pdf('test3.pdf')
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
        print(f"Estimated price: ${price:.5f}")
        
    except Exception as e:
        print(f"Error: {e}")
