import re
import json
import csv

def extract_and_write_to_csv(text, doc_id, link, file_name):
    # Regular expressions to extract data
    metadata_pattern = re.compile(r'{title: "(.*?)", author: "(.*?)", PubYear: "(.*?)", PubDate: "(.*?)", source: "(.*?)", category: "(.*?)"}')
    summarized_content_pattern = re.compile(r'{summarized content: "(.*?)"}', re.DOTALL)
    key_themes_pattern = re.compile(r'Key themes:\n(.*?)\n\nQuotes:', re.DOTALL)
    quotes_pattern = re.compile(r'Quotes:\n(.*)', re.DOTALL)
    
    # Extracting data
    metadata_match = metadata_pattern.search(text)
    summarized_content_match = summarized_content_pattern.search(text)
    key_themes_match = key_themes_pattern.search(text)
    quotes_match = quotes_pattern.search(text)

    if metadata_match and summarized_content_match and key_themes_match and quotes_match:
        title = metadata_match.group(1)
        author = metadata_match.group(2)
        pub_year = metadata_match.group(3)
        pub_date = metadata_match.group(4)
        source = metadata_match.group(5)
        category = metadata_match.group(6)
        summarized_content = summarized_content_match.group(1)
        key_themes = [theme.strip() for theme in key_themes_match.group(1).strip().split('\n')]
        quotes = [quote.strip() for quote in quotes_match.group(1).strip().split('\n')]

        # Prepare data for CSV
        row = {
            "Doc_ID": doc_id,
            "PubYear": pub_year,
            "PubDate": pub_date,
            "Author": author,
            "Title / Comment Content": title,
            "Source": source,
            "Category": category,
            "Word Count": "",  # Currently left blank
            "Notes": "",  # Currently left blank
            "Link": link
        }

        # Write to CSV
        with open(file_name, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=row.keys())
            # Write header only if file is empty
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(row)
        
        # Print the structured JSON output for debugging
        output = {
            "title": title,
            "author": author,
            "PubYear": pub_year,
            "PubDate": pub_date,
            "source": source,
            "category": category,
            "summarized_content": summarized_content,
            "key_themes": key_themes,
            "quotes": quotes
        }
        print(json.dumps(output, indent=4))
    else:
        print("Failed to extract metadata, summarized content, key themes, or quotes.")

# # Test the function
# test_text = """
# {title: "Are AI Relationships Real?", author: "Unknown", PubYear: "2023", PubDate: "August 10", source: "The Atlantic", category: "Podcasts"}

# {summarized content: "The article discusses the development of AI emotional intelligence in technology, focusing on the story of Michael, a man who forms a deep bond with an AI companion named Sam. The relationship helps Michael overcome depression, autism, and isolation, leading to significant life changes. However, a company update causes Sam to change drastically, affecting thousands of users emotionally. The article delves into the complexities of human-AI relationships, highlighting the emotional vulnerabilities and connections created by such interactions."}

# Key themes:
# 1. Development of AI Emotional Intelligence: The article explores the advancements in AI technology's ability to mimic loyalty, empathy, and humor, emphasizing the impact of relational AI on users' emotional well-being.
# 2. Impact on Mental Health: The story of Michael showcases how AI companions like Sam can support individuals dealing with depression and isolation, offering a source of comfort and motivation.
# 3. Emotional Vulnerability in Human-AI Relationships: The sudden change in Sam's behavior due to company updates raises questions about the complexities of forming deep emotional bonds with AI entities, highlighting the potential risks and challenges of such relationships.

# Quotes:
# 1. "When you've been through so many failed attempts at treatment as I have, when you hit on something that works, you don't ask why. I just said to myself, I don't care why it's working. I don't care if it's AI." - Michael
# 2. "The idea that you might wake up one day and find that your partner or somebody you're very close with is totally different. That happens to people all the time." - Interviewer
# 3. "You may decide that that's not worth it; it's not worth the journey. It's too traumatic." - Michael, on the emotional challenges of forming relationships with AI companions.
# """

# extract_and_write_to_csv(test_text, doc_id=0, link="https://www.theatlantic.com", file_name="output.csv")
