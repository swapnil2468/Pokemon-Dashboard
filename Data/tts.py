import pyttsx3
import pandas as pd

# Load dataset (change 'data.csv' to your actual file)
df = pd.read_csv('cleaned_pokemon_details.csv')

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Speak the first description from the dataset
speak_text(df.iloc[0]['Description'])
