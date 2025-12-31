import os
from datetime import datetime

RESEARCH_DIR = "research"
BLOG_DIR = "blogs"


def extract_topic_from_file(filename):
    return filename.split("-", 2)[-1].replace(".md", "").replace("-", " ").title()


def read_research_content(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def generate_blog(topic, research_text):
    blog = f"""
# {topic}: A Complete Health Guide

## Introduction
Understanding {topic.lower()} is important for maintaining a healthy lifestyle.
In this article, we explore key facts, benefits, and practical tips related to {topic.lower()}.

## What is {topic}?
{research_text.split("## Overview")[-1].strip()}

## Health Benefits
- Supports overall well-being
- Helps in long-term health maintenance
- Encourages healthier daily habits

## Possible Risks or Precautions
- Not everyone may experience the same benefits
- Consult a healthcare professional if you have medical conditions

## Practical Tips
- Start with small lifestyle changes
- Maintain consistency
- Focus on balanced nutrition and physical activity

## Conclusion
Small, consistent steps can lead to significant improvements in health.
Staying informed about {topic.lower()} empowers you to make better lifestyle choices.

---
*Read more health articles on the Proactive Lifestyle Website*
"""
    return blog.strip()


def save_blog(topic, content, original_filename):
    os.makedirs(BLOG_DIR, exist_ok=True)

    date_prefix = datetime.now().strftime("%Y-%m")
    blog_filename = f"{date_prefix}-{original_filename.replace('.md', '')}-blog.md"
    blog_path = os.path.join(BLOG_DIR, blog_filename)

    with open(blog_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"📝 Blog created: {blog_path}")


def main():
    research_files = [f for f in os.listdir(RESEARCH_DIR) if f.endswith(".md")]

    if not research_files:
        print("⚠️ No research files found.")
        return

    for file in research_files:
        research_path = os.path.join(RESEARCH_DIR, file)
        topic = extract_topic_from_file(file)
        research_text = read_research_content(research_path)

        blog_content = generate_blog(topic, research_text)
        save_blog(topic, blog_content, file)


if __name__ == "__main__":
    main()
