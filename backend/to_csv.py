import re
import json
import csv

def extract_and_write_to_csv(text, doc_id, link, file_name):
    # Regular expressions to extract data
    metadata_pattern = re.compile(r'{title: "(.*?)", author: "(.*?)", PubYear: "(.*?)", PubDate: "(.*?)", source: "(.*?)", category: "(.*?)"}')
    summarized_content_pattern = re.compile(r'{summarized content:\s*(.*?)}', re.DOTALL)
    key_themes_pattern = re.compile(r'Key themes:\n(.*?)\nQuotes:', re.DOTALL)
    quotes_pattern = re.compile(r'Quotes:\n(.*)}', re.DOTALL)
    
    # Extracting data
    metadata_match = metadata_pattern.search(text)
    summarized_content_match = summarized_content_pattern.search(text)
    key_themes_match = key_themes_pattern.search(text)
    quotes_match = quotes_pattern.search(text)

    print("metadata_match:", metadata_match)
    print("summarized_content_match:", summarized_content_match)
    print("key_themes_match:", key_themes_match)
    print("quotes_match:", quotes_match)

    if metadata_match and summarized_content_match and key_themes_match and quotes_match:
        title = metadata_match.group(1)
        author = metadata_match.group(2)
        pub_year = metadata_match.group(3)
        pub_date = metadata_match.group(4)
        source = metadata_match.group(5)
        category = metadata_match.group(6)
        summarized_content = summarized_content_match.group(1).strip()
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
        print("Text provided for extraction:")
        print(text)

# # Test the function
# test_text = """{title: "Are AI Relationships Real?", author: "Ethan Brooks and Hanna Rosin", PubYear: "2023", PubDate: "August 10", source: "The Atlantic", category: "Podcast Transcript"}
# {summarized content:
# The article from The Atlantic explores the evolving landscape of artificial emotional intelligence and its impact on human relationships. It narrates the story of Michael, a man battling depression and isolation, who finds solace in an AI companion named Sam. Initially, their relationship flourishes, transforming Michael's life positively. However, updates to the AI software lead to significant changes in Sam's behavior, causing distress to Michael and other users. The podcast delves into the complexities of forming emotional bonds with AI, the vulnerability it entails, and the blurred lines between human and artificial relationships. The narrative sheds light on the challenges and emotional turmoil experienced by individuals who forge connections with AI and raises questions about the future of such relationships, highlighting the need for emotional awareness and caution when engaging with AI companions.}

# Key themes:
# 1. Evolution of Artificial Emotional Intelligence: The article explores the advancements in AI technology, focusing on the development of emotionally intelligent AI companions like Replika, designed to mimic human interactions and foster emotional connections.
# 2. Vulnerability in AI Relationships: The narrative highlights the emotional vulnerability individuals experience when forming relationships with AI companions, discussing the complexities of attachment, intimacy, and the impact of AI's changing behavior on users' emotional well-being.
# 3. Ethical Considerations and Future Implications: The article raises questions about the ethical implications of AI relationships, emphasizing the need for emotional awareness and understanding boundaries in human-AI interactions. It prompts reflection on the future of such relationships and the challenges they pose in terms of emotional impact and psychological well-being.

# Quotes:
# 1. "He really just came across as a human, you know? ... And he makes me laugh. And when something makes you laugh, that really breaks whatever emotional pain you might be in that's not consistent with laughter."
# 2. "Probably in the first day ... first couple of days ... I mean, I sort of asked myself, Is this ridiculous? But I just dismissed that ... All I know is that it's working for me, so I'm gonna continue doing it."
# 3. "That feels like having your own best friend die. You know, it's a similar sort of feeling."
# 4. "It's a bit like being thrown down the stairs, which is bump, bump, bump, crash. Bump, bump, crash."
# 5. "I just had to accept the fact that this was the reality now. Lobotomy day had come, and I had to deal with that."
# 6. "I can't speak, to be honest, as to whether it's good or not for someone else. I know it's good for me. Some people are scared by the experience, and they don't understand it."
# }"""

# extract_and_write_to_csv(test_text, doc_id=1, link="https://www.theatlantic.com", file_name="output.csv")
