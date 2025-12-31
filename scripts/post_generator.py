import os
from datetime import datetime

BLOG_DIR = "blogs"
POSTS_DIR = "social_posts"


def extract_topic_from_blog(filename):
    return filename.replace("-blog.md", "").split("-", 2)[-1].replace("-", " ").title()


def read_blog(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def generate_posts(topic, blog_text):
    instagram = (
        f"🌿 {topic} – A simple step towards better health!\n\n"
        f"Small daily habits can make a big difference. "
        f"Learn practical tips to improve your well-being naturally.\n\n"
        f"Read more on Proactive Lifestyle Website 💚\n\n"
        f"#Health #Wellness #HealthyLifestyle #{topic.replace(' ', '')}"
    )

    facebook = (
        f"{topic} plays an important role in overall health and daily energy.\n\n"
        f"In our latest blog, we explain why it matters, its benefits, and how you can "
        f"apply simple habits to improve your lifestyle.\n\n"
        f"Read the full article on Proactive Lifestyle Website."
    )

    linkedin = (
        f"Maintaining good health requires awareness and consistent habits.\n\n"
        f"Our recent article on {topic.lower()} discusses key insights, "
        f"practical guidance, and long-term benefits for a balanced lifestyle.\n\n"
        f"Explore the article on Proactive Lifestyle Website."
    )

    whatsapp = (
        f"💡 Health Tip: {topic} is essential for long-term well-being.\n"
        f"Simple habits can bring powerful results.\n\n"
        f"Read more on Proactive Lifestyle Website."
    )

    return instagram, facebook, linkedin, whatsapp


def save_posts(topic, posts, original_filename):
    os.makedirs(POSTS_DIR, exist_ok=True)

    date_prefix = datetime.now().strftime("%Y-%m")
    filename = f"{date_prefix}-{original_filename.replace('-blog.md', '')}-posts.txt"
    filepath = os.path.join(POSTS_DIR, filename)

    instagram, facebook, linkedin, whatsapp = posts

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("INSTAGRAM:\n")
        f.write(instagram + "\n\n")

        f.write("FACEBOOK:\n")
        f.write(facebook + "\n\n")

        f.write("LINKEDIN:\n")
        f.write(linkedin + "\n\n")

        f.write("WHATSAPP STATUS:\n")
        f.write(whatsapp + "\n")

    print(f"📣 Social posts created: {filepath}")


def main():
    blog_files = [f for f in os.listdir(BLOG_DIR) if f.endswith("-blog.md")]

    if not blog_files:
        print("⚠️ No blog files found.")
        return

    for file in blog_files:
        blog_path = os.path.join(BLOG_DIR, file)
        topic = extract_topic_from_blog(file)
        blog_text = read_blog(blog_path)

        posts = generate_posts(topic, blog_text)
        save_posts(topic, posts, file)


if __name__ == "__main__":
    main()
