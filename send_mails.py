import pandas as pd
import yagmail
import time
import os
import sys

# ================== CONFIG ==================

# Use environment variables (DO NOT hardcode credentials)
EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

if not EMAIL or not APP_PASSWORD:
    print("❌ ERROR: Please set EMAIL and APP_PASSWORD environment variables.")
    sys.exit()

RESUME_PATH = "Sample-resume.pdf"  # Keep resume in same folder

YOUR_NAME = "Your Name"

linkedin = "LinkdIn_Link"
github = "Github_Link"
portfolio = "Portfolio_Link"

# ============================================

# Read and clean HR list
try:
    df = pd.read_csv("HR_list_sample.csv", encoding="utf-8-sig")
    df.columns = df.columns.str.strip().str.lower()
except Exception as e:
    print(f"❌ Failed to read CSV: {e}")
    sys.exit()

required_columns = {"name", "email", "company"}
if not required_columns.issubset(set(df.columns)):
    print("❌ CSV must contain columns: name, email, company")
    sys.exit()

if not os.path.exists(RESUME_PATH):
    print("❌ Resume file not found.")
    sys.exit()
    
# Login to Gmail
try:
    yag = yagmail.SMTP(EMAIL, APP_PASSWORD)
except Exception as e:
    print(f"❌ Gmail login failed: {e}")
    sys.exit()

print("🚀 Starting email automation...\n")

total = len(df)
sent_count = 0

# Loop through HR list
for index, row in df.iterrows():
    name = str(row["name"]).strip()
    email = str(row["email"]).strip()
    company = str(row["company"]).strip()

    # Skip invalid emails
    if "@" not in email:
        print(f"⚠ Skipping invalid email: {email}")
        continue

    if not name or not company:
        print("⚠ Skipping incomplete row")
        continue

    subject = f"Application for AI / Data Scientist Role | Resume | {company}"

    body = f"""
Dear {name},

I hope you are doing well.

My name is {YOUR_NAME}, and I am a 3rd year student focused on AI, Machine Learning, and Data Analysis. I came across {company} and was impressed by your work.

I am actively looking for an internship / entry-level opportunity where I can contribute to real-world AI and data-driven projects.

You can view my work here:
Portfolio: {portfolio}
GitHub: {github}
LinkedIn: {linkedin}

Please find my resume attached for your consideration.

Thank you for your time.

Warm regards,
{YOUR_NAME}
"""

    try:
        yag.send(
            to=email,
            subject=subject,
            contents=body,
            attachments=RESUME_PATH
        )
        print(f"✅ Sent to {name} at {company}")
        sent_count += 1
        time.sleep(60)  # 60 sec delay to avoid spam detection

    except Exception as e:
        print(f"❌ Failed for {email}: {e}")

print(f"\n🎉 Process completed! {sent_count}/{total} emails sent successfully.")