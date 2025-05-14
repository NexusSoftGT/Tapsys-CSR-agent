# speak.py

import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play

load_dotenv()

# Initialize client
client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

# Optional: Set default voice and model
VOICE_ID = "JBFqnCBsd6RMkjVDRZzb"  # Replace with your voice ID
MODEL_ID = "eleven_multilingual_v2"
OUTPUT_FORMAT = "mp3_44100_128"

def speak_text(text):
    """Converts Roman Urdu text to voice and plays it"""
    audio = client.text_to_speech.convert(
        text=text,
        voice_id=VOICE_ID,
        model_id=MODEL_ID,
        output_format=OUTPUT_FORMAT,
    )
    play(audio)
    