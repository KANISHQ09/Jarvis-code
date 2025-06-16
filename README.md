# 🤖 Warrivo - Your Personal Desktop AI Assistant

Warrivo is a Python-based voice assistant that listens to your commands and performs actions like searching Wikipedia, sending emails, opening apps/websites, telling time/date/day, and even sending WhatsApp messages!

## 🌟 Features

* 🎤 Voice Command Recognition using `speech_recognition`
* 🗣️ Text-to-Speech via `pyttsx3`
* 🌐 Opens Websites like YouTube, Google, Instagram, etc.
* 📆 Tells current date, day, and time
* 🎵 Plays music from local directory
* 📧 Sends emails using SMTP
* 💬 Sends scheduled WhatsApp messages
* 🧠 Wikipedia summary search
* ⚙️ Launches apps like Calculator, Brave, Spotify

## 🛠️ Tech Stack

* Python 3.x
* `pyttsx3`
* `speech_recognition`
* `wikipedia`
* `webbrowser`, `os`, `datetime`, `calendar`
* `smtplib` (for sending emails)
* `pywhatkit` (for WhatsApp messages)
* `subprocess` (for app launching)

## 📦 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/warrivo.git
cd warrivo
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, install manually:

```bash
pip install pyttsx3 speechrecognition wikipedia pywhatkit
```

3. **(Optional)** Make sure you have access to a microphone and an internet connection (for API-based services).

## ▶️ How to Run

```bash
python warrivo.py
```

Once started, Warrivo will greet you and begin listening for voice commands.

## 🔐 Email Setup

If you're using Gmail to send emails:

* Go to your Gmail account settings
* Enable "Less Secure Apps" or set up an [App Password](https://myaccount.google.com/apppasswords)
* Replace the email and password in `sendEmail()` with your credentials:

```python
server.login('youremail@gmail.com', 'your-app-password')
```

## 📁 Customization

### Change App Paths:

Modify these lines to point to actual app shortcuts on your PC:

```python
os.startfile('C:\\Users\\Asus\\Desktop\\Spotify.lnk')
```

### Change Music Directory:

Update `music_dir` with the actual folder path where your songs are located.

```python
music_dir = 'C:\\Users\\YourName\\Music'
```

### WhatsApp Message:

Adjust phone number and time:

```python
pywhatkit.sendwhatmsg("+91xxxxxxxxxx", "hello", 18, 3)
```

## 💡 Example Commands

| Say...                        | Result                        |
| ----------------------------- | ----------------------------- |
| "Open YouTube"                | Opens youtube.com             |
| "Search Wikipedia for Python" | Speaks summary about Python   |
| "Send email to Kanishq"       | Sends email to preset address |
| "What’s the time"             | Tells the current time        |
| "Open calculator"             | Launches calculator app       |
| "Play music"                  | Plays music from folder       |
| "Send WhatsApp message"       | Schedules a message           |
| "Goodbye"                     | Exits the assistant           |

## 🔒 Notes

* For email and WhatsApp functions to work, ensure:

  * Gmail setup is correctly configured
  * Your system time is accurate
  * You are logged into WhatsApp Web
* Some features might not work on Mac/Linux without modification.

## 📜 License

MIT License
