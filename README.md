# Health Content Automation System

## 📌 Project Overview
The Health Content Automation System is a Python-based automation project designed to generate health-related content automatically.  
It performs topic research, blog creation, and social media post generation using a modular and ethical automation approach.

This system is built for:
- College final year project submission
- Personal productivity
- Small business / content creation workflows

---

## 🎯 Problem Statement
Creating high-quality health content requires extensive research, writing time, and consistency.  
Manual content creation is time-consuming and difficult to scale.

This project solves the problem by automating:
- Topic research
- Blog writing
- Social media content generation

while keeping **manual review and posting**, ensuring ethical and platform-safe usage.

---

## ⚙️ System Workflow

Topics List
↓
Research Module
↓
Blog Generator
↓
Social Media Post Generator
↓
Manual Review & Publishing


---

## 🧩 Project Modules

### 1️⃣ Research Module
- Reads health topics from a text file
- Generates structured research content
- Saves output as research files

**Output Folder:** `research/`

---

### 2️⃣ Blog Generator Module
- Converts research into detailed blog content
- Uses clean formatting and logical flow
- Generates human-readable health blogs

**Output Folder:** `blogs/`

---

### 3️⃣ Social Media Post Generator
- Generates platform-specific posts for:
  - Instagram
  - Facebook
  - LinkedIn
  - WhatsApp Status

**Output Folder:** `social_posts/`

---

## 🛠️ Technologies Used
- Python 3.14+
- Virtual Environment (venv)
- File-based automation
- No paid APIs
- No external automation risks

---

## 🚀 How to Run the Project

1. Activate virtual environment  
2. Add topics in `topics/topics.txt`
3. Run full automation:

```bash
python run_all.py
