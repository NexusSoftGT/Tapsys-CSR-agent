import requests

GROQ_API_KEY = "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"
GROQ_TRANSCRIPTION_URL = "https://api.groq.com/openai/v1/audio/transcriptions"
AUDIO_FILE = "recorded_audio.wav"

def transcribe_audio():
    """Transcribes recorded audio using Groq API"""
    try:
        with open(AUDIO_FILE, "rb") as file:
            headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
            data = {
                "model": "whisper-large-v3",
                "temperature": "0",
                "response_format": "json",
                "language": "en",
                "prompt": "the text is about fintech: POS, payment, transaction, settlement, bank, account, money"
            }
            response = requests.post(GROQ_TRANSCRIPTION_URL, headers=headers, data=data, files={"file": file})

        if response.status_code == 200:
            return response.json().get("text", "No transcription found.")
        return "Transcription failed."

    except Exception as e:
        return f"Error: {str(e)}"
