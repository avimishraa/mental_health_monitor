import csv
import os
from datetime import datetime
from transformers import pipeline

# Load emotion classifier
emotion_classifier = pipeline(
    "text-classification", 
    model="j-hartmann/emotion-english-distilroberta-base", 
    top_k=1)

# Function to get valid user input for ratings
def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 5:
                return value
            else:
                print("Please enter a value between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

# Function to get user input for the daily log
def get_user_input():
    print("Please rate the following from 1 (low) to 5 (high):")
    mood = get_valid_input("1. How happy are you today? ")
    stress = get_valid_input("2. How stressed are you? ")
    energy = get_valid_input("3. How much energy do you have? ")
    sleep = get_valid_input("4. How well did you sleep last night? ")
    journal = input("5. Write a few words about how you're feeling today: ")

    # AI-powered emotion detection
    emotion_result = emotion_classifier(journal)
    emotion = emotion_result[0][0].get('label', 'neutral')
    if not emotion:
        emotion = "neutral"  # Default to neutral if no emotion detected
        
    return {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "mood": mood,
        "stress": stress,
        "energy": energy,
        "sleep": sleep,
        "emotion": emotion,
        "journal": journal
    }

# Function to provide personalized feedback based on user input
def feedback(entry):
    print(f"\n🧠 Detected Emotion: {entry['emotion']}")
    
    # Personalized feedback based on user input
    if entry["mood"] <= 2 or entry["stress"] >= 4:
        print("⚠️ You might be feeling low or stressed. Consider taking a break or talking to someone.")
    elif entry["energy"] <= 2:
        print("💡 You're feeling a bit tired. Rest up and drink some water!")
    else:
        print("😊 You're doing well! Keep up the good work!")
    
    # If sadness or anger detected, suggest talking to someone
    if entry["emotion"] in ["sadness", "anger"]:
        print("😔 It might help to talk to a friend or jot down your feelings. You're not alone.")

# Directory for log files
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

filename = os.path.join(log_dir, "mental_health_log.csv")

# Function to save the entry into a CSV file
def save_entry(entry, filename=filename):
    file_exists = os.path.exists(filename)

    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=entry.keys())
        if not file_exists:
            writer.writeheader()  # Write header only if file doesn't exist
        writer.writerow(entry)

# Main program
if __name__ == "__main__":
    data = get_user_input()
    save_entry(data)
    feedback(data)
