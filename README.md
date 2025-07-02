# 🎮 Roblox Account Checker

![Python](https://img.shields.io/badge/Python-3.8%2B-yellow?style=for-the-badge&logo=python)
![Selenium](https://img.shields.io/badge/Selenium-Automation-brightgreen?style=for-the-badge&logo=selenium)
![ChromeDriver](https://img.shields.io/badge/ChromeDriver-Supported-blue?style=for-the-badge&logo=googlechrome)
![GitHub Stars](https://img.shields.io/github/stars/nautherteam/roblox-checker?style=for-the-badge)

---

![Roblox Checker Preview](https://images.rbxcdn.com/d66ae37d46e00a1ecacfe9531986690a.jpg)

---

## 🚀 About the Project

**Roblox Account Checker** is a lightweight, powerful tool built with **Python + Selenium** to perform **automated mass-checking of Roblox accounts**. It reads a combo list (`username/email:password`) and checks which accounts are valid through browser automation.

Use cases include:

- Personal account audits
- Recovery validation
- Educational purposes in cybersecurity

---

## ⚙️ Features

- ✅ Supports both `username:password` and `email:password`
- 🔁 Multithreaded for speed and performance
- 🔐 Uses official https://roblox.com/login endpoint
- 👁️‍🗨️ Optional headless mode
- 📊 Real-time output with colored status
- 📁 Easily customizable and open-source

---

## 📂 Folder Structure

```
roblox-checker/
├── main.py                # Main checker script
├── combo.txt              # Input file with combos
├── chromedriver.exe       # ChromeDriver (add or download manually)
└── README.md              # This file
```

---

## 📦 Installation

### 🔧 Requirements

- ✅ Python 3.8 or newer
- ✅ Google Chrome (installed)
- ✅ ChromeDriver matching your Chrome version (https://chromedriver.chromium.org/downloads)

---

### 🧪 Setup Instructions

```bash
git clone https://github.com/nautherteam/roblox-checker.git
cd roblox-checker
pip install -r requirements.txt
```

Place your combos in `combo.txt` like this:

```
username1:password1
email2:password2
username3:password3
```

---

### 🚀 Run the Tool

```bash
python main.py
```

> ✅ The tool will start launching Chrome instances, checking each account one-by-one or in parallel depending on configuration.

---

## 🎨 Output Legend

| Status     | Meaning                | Console Color |
| ---------- | ---------------------- | ------------- |
| ✅ Valid   | Login successful       | 🟢 Green      |
| ❌ Invalid | Credentials don't work | 🔴 Red        |
| ⚠️ Error   | Timeout, Captcha, etc. | 🟡 Yellow     |

---

## 🧩 Example Output

```
[✓] Valid:    noobgamer123:abc12345
[✗] Invalid:  guesttester44:wrongpass
[!] Error:    probuilder:blocked by captcha
```

---

## 🔄 Troubleshooting

| Issue                         | Solution                                                              |
| ----------------------------- | --------------------------------------------------------------------- |
| selenium.common.exceptions.\* | Ensure Chrome & ChromeDriver versions match                           |
| Script closes too fast        | Run via terminal/command prompt to view results                       |
| Only checks 1 combo           | Make sure `combo.txt` has multiple lines and proper formatting        |
| Captcha blocks all attempts   | Add delay or reduce thread count; captchas are designed to stop abuse |

---

## 🤝 Contributing

Want to improve the script or add features (e.g., proxy support, GUI, etc)?  
We welcome contributions!

```
# Fork this repo
# Create a new branch
# Commit your changes
# Submit a pull request
```

---

## 📜 License

This project is licensed under the **MIT License**.  
See `LICENSE` file for details.

---

## ⚠️ Disclaimer

> This project is for **educational and ethical purposes only**.  
> You are responsible for how you use this tool.  
> Do **not** use it to access accounts without **explicit permission**.

---

## 📫 Contact

Created by **Nauther**  
GitHub: [@nautherteam](https://github.com/nautherteam)

---

**Game smart. Code smarter. 🚀**
