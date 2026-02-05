# 📲 WhatsApp Automated Message Scheduler (Python + Twilio)

A Python-based application that allows users to schedule and send WhatsApp messages at a specific date and time using the Twilio WhatsApp Sandbox.

---

## 🚀 Features

- Schedule WhatsApp messages for a future date & time
- Uses Twilio WhatsApp Sandbox
- Secure credential handling using environment variables
- Beginner-friendly and easy to extend

---

## 🛠️ Tech Stack

- Python 3
- Twilio API
- python-dotenv
- WhatsApp Sandbox

---

## 📂 Project Structure

```
whatsapp-automated-message/
│
├── main.py
├── requirements.txt
├── .gitignore
├── .env        # not pushed to GitHub
└── README.md
```

---

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/whatsapp-automated-message.git
cd whatsapp-automated-message
```

### 2️⃣ Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3️⃣ Create `.env` file

Create a `.env` file in the root directory and add:

```
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=your_auth_token_here
```

---

##📲 WhatsApp Sandbox Setup (Important)

1. Go to **Twilio Console → WhatsApp Sandbox**
2. Save the sandbox number:

```
+14155238886
```

3. From your WhatsApp, send:

```
join <sandbox-code>
```

---

## ▶️ Run the Project

```bash
python main.py
```

Follow the prompts to:

- Enter recipient name
- Enter WhatsApp number
- Enter message
- Set date & time

---

## 🧪 Example Use Cases

- Schedule reminders
- Automated greetings
- Internship / demo project for APIs

---

## 🔒 Security Note

- Twilio credentials are stored in `.env`
- `.env` is ignored using `.gitignore`
- No secrets are exposed on GitHub

---

## 👤 Author

**Shravan Manekar**

