import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)

message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1000,
    temperature=0,
    system="You are a text summarization expert. Your task is to provide a concise and accurate summary of the main content of a webpage. Ignore any irrelevant text such as cookies notices, advertisements, navigation menus, or any other non-essential content. Focus only on the main article or core content of the page.\n",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Title: {extracted_title}\n\nMain Content: {extracted_text}\n\nPlease provide a summary of the above main content."
                }
            ]
        }
    ]
)
print(message.content)