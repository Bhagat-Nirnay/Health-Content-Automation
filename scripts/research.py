import os
import requests
from datetime import datetime

HEADERS = {
    "User-Agent": "HealthContentAutomation/1.0 (contact: proactive.lifestyle@example.com)"
}

# -------------------------------
# CONFIGURATION
# -------------------------------
TOPICS_FILE = "topics/topics.txt"
OUTPUT_DIR = "research"

WIKIPEDIA_API_URL = "https://en.wikipedia.org/api/rest_v1/page/summary/"


# -------------------------------
# UTILITY FUNCTIONS
# -------------------------------
def slugify(text):
    """Convert topic into file-safe name"""
    return text.lower().strip().replace(" ", "-").replace("/", "").replace(",", "")


def read_topics(file_path):
    """Read topics from file"""
    with open(file_path, "r", encoding="utf-8") as f:
        topics = [line.strip() for line in f if line.strip()]
    return topics


def fetch_wikipedia_summary(topic):
    """
    Reliable Wikipedia search + summary fetch using MediaWiki API
    """

    # Step 1: Search for the topic
    search_url = "https://en.wikipedia.org/w/api.php"
    search_params = {
        "action": "query",
        "list": "search",
        "srsearch": topic,
        "format": "json",
    }

    search_response = requests.get(search_url, params=search_params, headers=HEADERS)

    if search_response.status_code != 200:
        return None

    search_data = search_response.json()
    search_results = search_data.get("query", {}).get("search", [])

    if not search_results:
        return None

    # Take the best matching page title
    page_title = search_results[0]["title"]

    # Step 2: Fetch summary for that page
    summary_url = (
        "https://en.wikipedia.org/api/rest_v1/page/summary/"
        + page_title.replace(" ", "_")
    )
    summary_response = requests.get(summary_url, headers=HEADERS)

    if summary_response.status_code != 200:
        return None

    summary_data = summary_response.json()
    return summary_data.get("extract")


def save_research(topic, content):
    """Save research to markdown file"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    date_prefix = datetime.now().strftime("%Y-%m")
    filename = f"{date_prefix}-{slugify(topic)}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# Research: {topic}\n\n")
        f.write("## Overview\n")
        f.write(content + "\n\n")
        f.write("## Source\n")
        f.write("- Wikipedia\n")

    print(f"✅ Research saved: {filepath}")


# -------------------------------
# MAIN EXECUTION
# -------------------------------
def main():
    topics = read_topics(TOPICS_FILE)

    if not topics:
        print("⚠️ No topics found.")
        return

    for topic in topics:
        print(f"\n🔍 Researching: {topic}")
        summary = fetch_wikipedia_summary(topic)

        if summary:
            save_research(topic, summary)
        else:
            print(f"❌ No data found for: {topic}")


if __name__ == "__main__":
    main()
