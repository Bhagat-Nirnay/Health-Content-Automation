from fastapi import FastAPI
from datetime import datetime
import subprocess

app = FastAPI()


def log_run(message):
    with open("logs/execution.log", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | {message}\n")


@app.post("/run automation")
def run_automation():
    try:
        subprocess.run(
            [
                "D:/health-content-automation/venv/Scripts/python.exe",
                "D:\health-content-automation/run_all.py",
            ],
            check=True,
        )
        return {
            "status": "success",
            "message": "Automation completed",
            "generated": {
                "research": research_file,
                "blog": blog_file,
                "social_posts": posts_file,
            },
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}
