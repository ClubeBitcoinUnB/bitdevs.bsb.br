# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-dotenv",
#     "dspy",
#     "requests",
# ]
# ///

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

# lm = dspy.LM(model="openai/gpt-4o-mini")
lm = dspy.LM(
    model="openrouter/deepseek/deepseek-r1-0528-qwen3-8b",
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
    return dspy.Predict("title: str -> is_date: bool")(title=title).is_date

# Original function
get_theme_text_link = dspy.Predict("comment: str -> theme: THEMES, exact_text: str, link: str", 
    instructions="Infer theme of the comment, and return exact text and link of the comment as they are, without any changes.")


get_theme = dspy.Predict("comment_text: str -> theme: THEMES")


def scrape_github_issues_api():
    """Get issues using GitHub API"""
    # Optional: use GitHub token for higher rate limits
    token = os.getenv('GITHUB_TOKEN')  # Add this to your .env file
    headers = {'Authorization': f'token {token}'} if token else {}
    
    url = "https://api.github.com/repos/BitDevsBSB/BitDevsBSB/issues"
    response = requests.get(url, headers=headers)
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
    issue_url = f"https://api.github.com/repos/BitDevsBSB/BitDevsBSB/issues/{issue_number}"
    issue_response = requests.get(issue_url, headers=headers)
    issue_response.raise_for_status()
    issue_data = issue_response.json()
    
    # Get comments
    comments_url = f"https://api.github.com/repos/BitDevsBSB/BitDevsBSB/issues/{issue_number}/comments"
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

def main():
    log_filename = 'aux/agenda_generator.log'
    json_filename = 'aux/agenda.json'

    logging.basicConfig(filename=log_filename,
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filemode='w')

    logging.info("Scraping GitHub issues from BitDevsBSB/BitDevsBSB...")

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

            comment_content = comment['content']
            link = get_link(comment_content)
            text = get_text(comment_content, link)
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

        themed_agenda = defaultdict(list)
        for item in agenda_items:
            if item['link'] and item['text']:
                bullet_point = f"* [{item['text']}]({item['link']})"
            elif item['text']:
                bullet_point = f"* {item['text']}"
            elif item['link']:
                bullet_point = f"* {item['link']}"
            else:
                continue
            themed_agenda[item['theme']].append(bullet_point)

        with open(json_filename, 'w', encoding='utf-8') as f:
            json.dump(themed_agenda, f, ensure_ascii=False, indent=4)

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



