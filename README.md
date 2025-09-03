# ANM IT Support Tools

A collection of IT support tools and resources built to streamline common support tasks, monitoring, and troubleshooting.  
This project includes scripts, guides, and a lightweight **Flask-powered IT Dashboard** for real-time system metrics and device status.

---

## Features

- 📊 **IT Monitoring Dashboard** (Flask + psutil)  
  - Displays **CPU and memory usage**  
  - Shows network device status (e.g., router, printer, server)  
  - Auto-refreshes to keep data up to date  

- ⚡ **Scripts for IT Support**  
  - Python and PowerShell utilities for common tasks  
  - Example: network checks, AD user management, and more  

- 📚 **Troubleshooting Guides**  
  - Step-by-step markdown documents for recurring IT issues  
  - Example: printer issues, email problems  

---

## Project Structure

ANM-IT-Support-Tools/
│
├── Dashboard/ # Flask web dashboard
│ ├── app.py
│ ├── dashboard-screenshot.png
│ ├── dashboard-demo.gif
│ └── static/
│ └── style.css
│
├── Scripts/ # Python / PowerShell scripts
│ └── ...
│
├── Troubleshooting-Guides/ # Markdown IT troubleshooting guides
│ ├── Printer-Troubleshooting.md
│ └── Email-Issues.md
│
└── README.md # Project overview

yaml
Copy code

---

## Setup & Usage

### 1. Clone the repository

```bash
git clone https://github.com/Garytech64/ANM-IT-Support-Tools.git
cd ANM-IT-Support-Tools
2. Run the Dashboard
bash
Copy code
cd Dashboard
pip install flask psutil
python app.py
Open your browser and go to:
👉 http://127.0.0.1:5000/

Demo
Screenshot:


Animated Demo:


Troubleshooting Guides
Printer Troubleshooting

Email Issues

Future Improvements
🔧 Integrate real network device checks (ping, SNMP, etc.)

📡 Expand dashboard metrics (disk usage, uptime, alerts)

🖥️ Add user authentication for dashboard access

🌐 Deploy on an internal server for shared team use

Author
👨‍💻 Created by Gary Aitken
IT Engineer | Passionate about automation, support tools, and monitoring solutions

yaml
Copy code

---

✅ Now your **screenshot and GIF will render properly** instead of being green text.  

Would you like me to also draft a **LinkedIn post caption** you can use to showcase this project once it’s live on GitHub?






You said:
can you put everthing in one readme file i can copy and pste into local file


ChatGPT said:
Absolutely, Gaz 👍
Here’s the full, clean README.md in one block — just copy/paste it into your local README.md file.

ANM IT Support Tools
A collection of IT support tools and resources built to streamline common support tasks, monitoring, and troubleshooting.
This project includes scripts, guides, and a lightweight Flask-powered IT Dashboard for real-time system metrics and device status.

Features
📊 IT Monitoring Dashboard (Flask + psutil)

Displays CPU and memory usage

Shows network device status (e.g., router, printer, server)

Auto-refreshes to keep data up to date

⚡ Scripts for IT Support

Python and PowerShell utilities for common tasks

Example: network checks, AD user management, and more

📚 Troubleshooting Guides

Step-by-step markdown documents for recurring IT issues

Example: printer issues, email problems

Project Structure
csharp
Copy code
ANM-IT-Support-Tools/
│
├── Dashboard/                  # Flask web dashboard
│   ├── app.py
│   ├── dashboard-screenshot.png
│   ├── dashboard-demo.gif
│   └── static/
│       └── style.css
│
├── Scripts/                    # Python / PowerShell scripts
│   └── ...
│
├── Troubleshooting-Guides/     # Markdown IT troubleshooting guides
│   ├── Printer-Troubleshooting.md
│   └── Email-Issues.md
│
└── README.md                   # Project overview
Setup & Usage
1. Clone the repository
bash
Copy code
git clone https://github.com/Garytech64/ANM-IT-Support-Tools.git
cd ANM-IT-Support-Tools
2. Run the Dashboard
bash
Copy code
cd Dashboard
pip install flask psutil
python app.py
Open your browser and go to:
👉 http://127.0.0.1:5000/

Demo
Screenshot:


Animated Demo:


Troubleshooting Guides
Printer Troubleshooting

Email Issues

Future Improvements
🔧 Integrate real network device checks (ping, SNMP, etc.)

📡 Expand dashboard metrics (disk usage, uptime, alerts)

🖥️ Add user authentication for dashboard access

🌐 Deploy on an internal server for shared team use

Author
👨‍💻 Created by Gary Aitken
IT Engineer | Passionate about automation, support tools, and monitoring solutions