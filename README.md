# 🧠 AI-Powered Mental Health Monitoring System

A Python-based tool for daily mental health tracking that leverages AI to detect emotions from journal entries. It collects mood, stress, energy, and sleep ratings, provides personalized feedback, and logs insights for self-awareness and reflection.

---

## 📌 Features

- ✅ **Daily Mental Health Tracking -** Track mood, stress, energy, and sleep levels.
- 🤖 **AI-Powered Emotion Detection -** Uses Hugging Face Transformers to detect emotions from text.
- 💬 **Personalized Feedback -** Offers suggestions based on emotional and numeric inputs.
- 📊 **Historical Logging -** Saves logs in CSV format for trend analysis.
- 🔒 **Offline & Private -** Works fully offline after the initial model download.
- 📁 **Auto-Organized Logs -** Stores data in a dedicated `logs/` directory.
- 🛡️ **Input Validation -** Prevents crashes and ensures clean data entry.

---

## 🛠️ Technologies Used

- **Python 3.8+**
- **Hugging Face Transformers**
- **Pretrained Model**: `j-hartmann/emotion-english-distilroberta-base`
- **CSV** for structured data storage
- **NLP Pipeline** for emotion classification

---

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/avimishraa/mental_health_monitor.git
   cd mental-health-monitor
   ```

2. **Install dependencies**  
   Make sure you have Python 3.8+ and pip installed.
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python mental_health_monitor.py
   ```

---

## ✏️ Sample Input & Output

**📥 Terminal Input:**
```
1. How happy are you today? 2
2. How stressed are you? 4
3. How much energy do you have? 2
4. How well did you sleep last night? 3
5. Write a few words about how you're feeling today:
I'm overwhelmed and hopeless. Nothing is helping.
```

**🤖 Output:**
```
🧠 Detected Emotion: sadness
⚠️ You might be feeling low or stressed. Consider taking a break or talking to someone.
😔 It might help to talk to a friend or jot down your feelings. You're not alone.
```

**🗂️ CSV Log (`logs/mental_health_log.csv`):**
```csv
date,mood,stress,energy,sleep,emotion,journal
2025-07-14,2,4,2,3,sadness,I'm overwhelmed and hopeless. Nothing is helping.
```

---

## 🧩 Project Structure

```
mental_health_monitor.py       # Main script
mental_health_monitor.ipynb    # Optional Jupyter notebook version
requirements.txt               # Python package dependencies
logs/
└── mental_health_log.csv      # Automatically generated log file
README.md                      # Project documentation
```

---

## 🔒 Privacy Note

Your data stays **local**. After downloading the AI model, no external connections are made. Your journal entries and logs are stored only on your machine.

---

## 📈 Future Improvements

- 📊 Visualizations using Matplotlib or Plotly
- 🖥️ GUI interface with Tkinter or Streamlit
- 🔔 Daily reminders via email or desktop notification
- 📉 Sentiment trend tracking and early warning alerts

---

## 👨‍💻 Author

**Avinash Mishra**  
[LinkedIn](https://www.linkedin.com/in/avinash-mishra)

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).
