import os, requests
from dotenv import load_dotenv
load_dotenv()
MAILGUN_DOMAIN = os.getenv("MAILGUN_DOMAIN")
MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
EMAIL_TO = os.getenv("EMAIL_TO")

def send_email(subject, plain_text, html_body):
    res = requests.post(
        f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
        auth=("api", MAILGUN_API_KEY),
        data={
            "from": f"Manga Notifier <mailgun@{MAILGUN_DOMAIN}>",
            "to": EMAIL_TO,
            "subject": subject,
            "text": plain_text,
            "html": html_body
        }
    )
    return res

def format_html(chapters):
    with open("templates/notification_email.html", "r") as f:
        template = f.read()

    card_html = ""
    for c in chapters:
        card_html += f"""
        <div style="margin-bottom: 16px;">
          <strong style="font-size:18px;">{c['title']} – chapter {c['number']}</strong><br/>
          <a href="{c['url']}" style="color:#1a73e8; text-decoration:none;">Read now</a>
        </div>
        """

    return template.replace("{{CHAPTERS}}", card_html)
