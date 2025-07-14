# 🧠 AI-Powered Mental Health Monitoring System

A Python-based mental health tracking tool that uses AI to detect emotions from journal entries, collects mood/stress/sleep/energy ratings, provides personalized feedback, and logs insights for self-awareness and reflection.

---

## 📌 Features

- ✅ Daily mental health tracking (mood, stress, energy, sleep)
- 🤖 AI-powered emotion detection using Hugging Face Transformers
- 💬 Personalized feedback based on your emotional and numeric input
- 📊 CSV logging for historical tracking and trend analysis
- 🔒 Fully offline and private (after first model download)
- 📁 Auto-organized log storage in a `logs/` directory
- 🛡️ Input validation to prevent crashes or invalid data

---

## 🛠️ Technologies Used

- Python 3.8+
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- Pretrained model: [`j-hartmann/emotion-english-distilroberta-base`](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base)
- CSV for structured logging
- Basic NLP pipeline for emotion classification

---

## 🚀 Getting Started

### 1. **Clone this repository**
```bash
git clone https://github.com/avimishraa/mental_health_monitor.git
cd mental-health-monitor
```

### 2. **Install required packages**
Ensure you have Python 3.8+ and pip installed. Then:
```bash
pip install -r requirements.txt
```

### 3. **Run the application**
```bash
python mental_health_monitor.py
```

---

## ✏️ Sample Input & Output

### 📥 Input (via terminal)
```
1. How happy are you today? 2  
2. How stressed are you? 4  
3. How much energy do you have? 2  
4. How well did you sleep last night? 3  
5. Write a few words about how you're feeling today:  
I'm overwhelmed and hopeless. Nothing is helping.
```

### 🤖 Output
```
🧠 Detected Emotion: sadness  
⚠️ You might be feeling low or stressed. Consider taking a break or talking to someone.  
😔 It might help to talk to a friend or jot down your feelings. You're not alone.
```

### 🗂️ CSV File (`logs/mental_health_log.csv`)
```csv
date,mood,stress,energy,sleep,emotion,journal
2025-07-14,2,4,2,3,sadness,I'm overwhelmed and hopeless. Nothing is helping.
```

---

## 🧩 Project Structure

```
mental_health_monitor.py       # Main program file
mental_health_monitor.ipynb    # Jupyter file
requirements.txt               # Install dependencies
logs/
└── mental_health_log.csv      # Automatically created and updated
README.md                      # You're here!
```

---

## 🔒 Privacy Note

This tool stores all data **locally** on your machine. No data is sent to any server after the Hugging Face model is downloaded.

---

## 📈 Future Improvements

- Trend visualizations using Matplotlib or Plotly
- GUI interface with Tkinter or Streamlit
- Daily reminders via email or desktop notification
- Sentiment trends and early warning detection

---

## 👨‍💻 Author

**Avinash Mishra**  
[LinkedIn](http://www.linkedin.com/in/%20avinash-mishra01)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

