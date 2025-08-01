
# 📬 Manga Chapter Email Notifier

Stay ahead of your favorite manga releases — automatically get notified via email whenever a new chapter drops.

This Python-based project checks for the latest chapters of selected manga titles (like **One Piece**, **Baki**, **Dragon Ball Super**, and **Kengan Omega**) using the [MangaDex API](https://api.mangadex.org) and optionally MangaFreak scraping for early releases. When new chapters are available, a sleek HTML email is sent to your inbox using [Mailgun](https://mailgun.com).

## 🚀 Features

- Monitor multiple manga series
- Detects new chapters only (no spam)
- Sends beautiful HTML email notifications
- Secure with Mailgun + `.env`
- Pythonic and cleanly modular
- Future-ready for scrapers, Discord bots, or push alerts

## 🛠 Project Structure

```
manga-notifier/
├── main.py                   # Main controller
├── requirements.txt          # Pip dependencies
├── .env                      # Your Mailgun credentials
├── data/
│   └── last_manga_chapters.json   # Tracks last seen chapters
├── templates/
│   └── notification_email.html    # Sleek HTML email template
└── utilities/
    ├── manga_util.py         # MangaDex / MangaFreak logic
    └── email_util.py         # Mailgun integration & formatter
```

## ⚙️ Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Create `.env`

```env
MAILGUN_API_KEY=key-xxxxxx
MAILGUN_DOMAIN=sandbox12345.mailgun.org
EMAIL_TO=you@example.com
```

> If you're using a Mailgun sandbox domain, be sure to verify the recipient email.

### 3. Run It

```bash
python main.py
```

If new chapters are available, you will receive an email.

### 4. Automate It (Optional)

Use GitHub Actions, cron, or Task Scheduler to run it hourly or daily.

## 📦 Coming Soon

- MangaFreak integration (for early releases)
- Discord notifications
- Pushbullet / Pushover integration
- Custom release day configs (e.g., “One Piece = Wednesday”)

## 💬 Credits & Inspiration

- Powered by the [MangaDex API](https://api.mangadex.org)
- Email handled via [Mailgun](https://www.mailgun.com/)
