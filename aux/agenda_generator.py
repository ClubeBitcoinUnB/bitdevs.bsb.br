#!/usr/bin/env -S uv run --script --python 3.12.3 
#
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-dotenv",
#     "dspy",
#     "requests",
# ]
# ///

"""
This script scrapes the GitHub issues from the ClubeBitcoinUnB/BitDevsBSB repository and generates an agenda for the next meeting.

You'll need to have `uv` installed and add an .env file with the following variables:

GITHUB_TOKEN=your_github_token
OPENROUTER_API_KEY=your_openrouter_api_key

Usage:
```bash
brew install uv # if you don't have uv installed
uv run --script aux/agenda_generator.py 
# or just
chmod +x aux/agenda_generator.py
./aux/agenda_generator.py
```
"""

import json
import logging
import os
import re
from collections import defaultdict
from typing import Literal

import dspy
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.github.com/repos/ClubeBitcoinUnB/BitDevsBSB/issues"


lm = dspy.LM(
    model="openrouter/deepseek/deepseek-r1-0528-qwen3-8b:free",
    api_base="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

dspy.configure(lm=lm)

THEMES = Literal['not technical', 
                 'Bitcoin L1', 
                 'Lightning and L2', 
                 'Ecash', 
                 'Mining', 
                 'Security', 
                 'Other']


def get_link(comment: str) -> str | None:
    """Extracts the first link from a comment string using regex."""
    if not comment:
        return None
    match = re.search(r'https?://\S+', comment)
    return match.group(0) if match else None


def get_text(comment: str, link: str) -> str:
    """Removes the link from the comment and strips whitespace."""
    if not comment:
        return ""
    if link:
        return comment.replace(link, '').strip()
    return comment.strip()


def is_date(title: str) -> bool:
    date_grams = [
        "jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez", # Portuguese
        "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec", # English
    ]
    for gram in date_grams:
        if gram in title.lower():
            return True
    return False
    # if above fails, the following is more flexible, as it uses a LLM to infer the date:
    # return dspy.Predict("title: str -> is_date: bool")(title=title).is_date

# Original function
get_theme_text_link = dspy.Predict("comment: str -> theme: THEMES, exact_text: str, link: str", 
    instructions="Infer theme of the comment, and return exact text and link of the comment as they are, without any changes.")


get_theme = dspy.Predict("comment_text: str -> theme: THEMES")


def scrape_github_issues_api():
    """Get issues using GitHub API"""
    # Optional: use GitHub token for higher rate limits
    token = os.getenv('GITHUB_TOKEN')  # Add this to your .env file
    headers = {'Authorization': f'token {token}'} if token else {}
    
    response = requests.get(API_URL, headers=headers)
    response.raise_for_status()
    
    issues = response.json()
    
    # Find the first open issue that looks like a date
    for issue in issues:
        if issue['state'] == 'open' and is_date(issue['title']):
            return issue['number']
    
    raise ValueError("No suitable issue found")

def scrape_issue_comments_api(issue_number):
    """Get issue and comments using GitHub API"""
    token = os.getenv('GITHUB_TOKEN')
    headers = {'Authorization': f'token {token}'} if token else {}
    
    # Get issue details
    issue_url = f"{API_URL}/{issue_number}"
    issue_response = requests.get(issue_url, headers=headers)
    issue_response.raise_for_status()
    issue_data = issue_response.json()
    
    # Get comments
    comments_url = f"{API_URL}/{issue_number}/comments"
    comments_response = requests.get(comments_url, headers=headers)
    comments_response.raise_for_status()
    comments_data = comments_response.json()
    
    logging.info("=" * 60)
    logging.info(f"Issue: {issue_data['title']}")
    logging.info(f"URL: {issue_data['html_url']}")
    logging.info("=" * 60)
    
    all_comments = []
    
    # Add issue body
    if issue_data['body']:
        all_comments.append({
            'author': issue_data['user']['login'],
            'content': issue_data['body'],
            'type': 'issue_body'
        })
    
    # Add comments
    for comment in comments_data:
        all_comments.append({
            'author': comment['user']['login'],
            'content': comment['body'],
            'type': 'comment'
        })
    
    return all_comments, issue_data['title']

def list_to_dict(agenda_items: list[dict[THEMES, str]]) -> dict[THEMES, list[str]]:
    agenda_dict = defaultdict(list)
    for item in agenda_items:
        if item['link'] and item['text']:
            bullet_point = f"* [{item['text']}]({item['link']})"
        elif item['text']:
            bullet_point = f"* {item['text']}"
        elif item['link']:
            bullet_point = f"* {item['link']}"
        else:
            continue
        agenda_dict[item['theme']].append(bullet_point)
    return agenda_dict

def generate_agenda(agenda_dict: dict[THEMES, list[str]]) -> dict:
    agenda = ""
    if 'not technical' in agenda_dict:
        agenda += "### Aquecimento\n"
        agenda += "\n".join(agenda_dict['not technical'])
        agenda += "\n\n"
    if 'Bitcoin L1' in agenda_dict:
        agenda += "### Bitcoin L1\n"
        agenda += "\n".join(agenda_dict['Bitcoin L1'])
        agenda += "\n\n"
    if 'Lightning and L2' in agenda_dict:
        agenda += "### Lightning and L2\n"
        agenda += "\n".join(agenda_dict['Lightning and L2'])
        agenda += "\n\n"
    if 'Ecash' in agenda_dict:
        agenda += "### Ecash\n"
        agenda += "\n".join(agenda_dict['Ecash'])
        agenda += "\n\n"
    if 'Mining' in agenda_dict:
        agenda += "### Mineração\n"
        agenda += "\n".join(agenda_dict['Mining'])
        agenda += "\n\n"
    if 'Security' in agenda_dict:
        agenda += "### Criptografia e Segurança\n"
        agenda += "\n".join(agenda_dict['Security'])
        agenda += "\n\n"
    if 'Other' in agenda_dict:
        agenda += "### Outros\n"
        agenda += "\n".join(agenda_dict['Other'])
        agenda += "\n\n"
    return agenda
    
    

def main():
    log_filename = 'aux/agenda_generator.log'
    json_filename = 'aux/agenda.json'
    md_filename = 'aux/agenda.md'

    logging.basicConfig(filename=log_filename,
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filemode='w')

    logging.info("Scraping GitHub issues from ClubeBitcoinUnB/BitDevsBSB...")

    try:
        issue_number = scrape_github_issues_api()
        all_comments, _ = scrape_issue_comments_api(issue_number)

        logging.info("=" * 60)
        logging.info("ALL COMMENTS:")
        logging.info("=" * 60)

        agenda_items = []

        for i, comment in enumerate(all_comments, 1):
            comment_type = "Issue Body" if comment['type'] == 'issue_body' else "Comment"
            logging.info(f"\n{comment_type} #{i}")
            logging.info(f"Author: {comment['author']}")
            logging.info("Content:")
            logging.info(comment['content'])

            link = get_link(comment['content'])
            text = get_text(comment['content'], link)
            theme_prediction = get_theme(comment_text=text)

            agenda_items.append({
                'theme': theme_prediction.theme,
                'text': text,
                'link': link
            })

            logging.info("Bullet point:")
            logging.info(f"  Theme: {theme_prediction.theme}")
            logging.info(f"  Text: {text}")
            logging.info(f"  Link: {link}")
            logging.info("-" * 40)

        agenda_dict = list_to_dict(agenda_items)
        with open(json_filename, 'w', encoding='utf-8') as f:
            json.dump(agenda_dict, f, ensure_ascii=False, indent=4)

        agenda = generate_agenda(agenda_dict)
        with open(md_filename, 'w', encoding='utf-8') as f:
            f.write(agenda)

        success_message = f"Successfully generated agenda and saved to {json_filename}"
        logging.info(success_message)
        print(success_message)
        print(f"Details logged to {log_filename}")

    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data: {e}")
        print(f"Error fetching data: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}", exc_info=True)
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()



