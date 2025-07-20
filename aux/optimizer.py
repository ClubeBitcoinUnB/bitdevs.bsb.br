# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-dotenv",
#     "dspy",
# ]
# ///

import os
from typing import Literal

import dspy
from dotenv import load_dotenv

load_dotenv()

# lm = dspy.LM(model="openai/gpt-4o-mini")
lm = dspy.LM(
    model="openrouter/deepseek/deepseek-r1-0528-qwen3-8b",
    # model="openrouter/moonshotai/kimi-dev-72b:free",
    api_base="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

dspy.configure(lm=lm)

THEMES = Literal['not technical', 'Bitcoin L1', 'Lightning and L2', 'Ecash', 'Mining', 'Security', 'Other']

get_theme_text_link = dspy.Predict("comment: str -> theme: THEMES, text_without_link: str, link: str", 
    instructions="Infer theme of the comment, and return exact text and link of the comment as they are, without any changes.")


# Training examples for optimization - using real GitHub issue comments
training_examples = [
    dspy.Example(
        comment='Wallet of Satoshi x Spark ("self-custodial")\n\nhttps://x.com/spark/status/1940168641301119094',
        theme="Lightning and L2",
        text_without_link='Wallet of Satoshi x Spark ("self-custodial")',
        link="https://x.com/spark/status/1940168641301119094"
    ).with_inputs('comment'),
    dspy.Example(
        comment="Whirlpool is back\n\nhttps://ashigaru.rs/news/announcement-whirlpool/",
        theme="Security",
        text_without_link="Whirlpool is back",
        link="https://ashigaru.rs/news/announcement-whirlpool/"
    ).with_inputs('comment'),
    dspy.Example(
        comment="BTC++ Insider Edition 📰\nhttps://x.com/niftynei/status/1940853386951393623",
        theme="not technical",
        text_without_link="BTC++ Insider Edition 📰",
        link="https://x.com/niftynei/status/1940853386951393623"
    ).with_inputs('comment'),
    dspy.Example(
        comment="bitch@\n\nhttps://x.com/jack/status/1941989435962212728",
        theme="not technical",
        text_without_link="bitch@",
        link="https://x.com/jack/status/1941989435962212728"
    ).with_inputs('comment'),
    dspy.Example(
        comment="Running Bitcoin - From Core to Code: A Comparison of Clients\n\nhttps://s3.us-east-1.amazonaws.com/1a1z.com/files/1A1z+-+Running+Bitcoin+-+Client+Comparison.pdf",
        theme="Bitcoin L1",
        text_without_link="Running Bitcoin - From Core to Code: A Comparison of Clients",
        link="https://s3.us-east-1.amazonaws.com/1a1z.com/files/1A1z+-+Running+Bitcoin+-+Client+Comparison.pdf"
    ).with_inputs('comment'),
]

# Define exact match metric
def exact_match_metric(example, pred, trace=None):
    """Exact match metric for theme, text, and link"""
    return (example.text_without_link == pred.text_without_link and 
            example.link == pred.link)

# for example in training_examples:
#     response = get_theme_text_link(comment=example.comment)
#     print(response)
#     print(example.theme == response.theme, example.theme)
#     print(example.text_without_link == response.text_without_link, example.text_without_link)
#     print(example.link == response.link, example.link)

#     if example.text_without_link != response.text_without_link:
#         same_chars = []
#         for i, char in enumerate(example.text_without_link):
#             if char == response.text_without_link[i]:
#                 same_chars.append(char)
#             else:
#                 same_chars.append(f"_{char}_")
#         print('*' * 5)
#         print("".join(same_chars))
#         print('*' * 5)

#     print("-" * 10)


##################### AI EVALUATION ###################################

# evaluate = Evaluate(devset=training_examples, num_threads=5)

# print("Evaluating original program...")
# evaluate(get_theme_text_link, metric=exact_match_metric)

##################### DETERMINISTIC EVALUATION ###################################

# total_correct = 0
# for example in training_examples:
#     text_without_link = get_text(example.comment, example.link)
#     link = get_link(example.comment)

#     if (example.text_without_link == text_without_link and
#         example.link == link):
#         total_correct += 1
#     else:
#         print(example.text_without_link == text_without_link, example.link == link)
#         print(example.text_without_link)
#         print(text_without_link)
#         print(example.link) 
#         print(link)
#         print("-" * 10)

# print("=" * 10)
# print(f'Total correct: {total_correct} / {len(training_examples)}')
# print("=" * 10)


##################### OPTIMIZATION ##################################

# optimizer = MIPROv2(metric=exact_match_metric, auto="medium", max_bootstrapped_demos=5)
# compiled_program = optimizer.compile(get_theme_text_link, trainset=training_examples)

# print("Evaluating compiled program...")
# evaluate(compiled_program, metric=exact_match_metric)

# print("Saving optimized program...")
# compiled_program.save("aux/optimized_model.json")

# print("Done!")
