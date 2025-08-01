from utilities.manga_util import get_latest_chapter
from utilities.email_util import send_email, format_html
import json, os
from datetime import datetime

TITLES = ["One Piece", "Baki", "Dragon Ball Super", "Kengan Omega", "One Punch Man", "Black Clover","Doctor Stone"]
DATA_FILE = "data/last_manga_chapters.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def main():
    last_data = load_data()
    new_data = last_data.copy()
    updates = []

    for title in TITLES:
        chapter = get_latest_chapter(title)
        if chapter and chapter["id"] != last_data.get(title, {}).get("id"):
            updates.append(chapter)
            new_data[title] = chapter

    if updates:
        subject = f"New Manga Chapter(s) Available! - {datetime.now().strftime('%d/%m/%y')}"
        plain_text = "\n".join(f"{c['title']} - Chapter {c['number']}: {c['url']}" for c in updates)
        html_body = format_html(updates)
        send_email(subject, plain_text, html_body)
        save_data(new_data)
    else:
        print("📖 No new chapters yet.")

if __name__ == "__main__":
    main()
