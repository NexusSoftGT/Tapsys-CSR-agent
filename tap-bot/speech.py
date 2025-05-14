import requests

GROQ_API_KEY = "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"
GROQ_TRANSCRIPTION_URL = "https://api.groq.com/openai/v1/audio/transcriptions"
AUDIO_FILE = "recorded_audio.wav"

def transcribe_audio():
    """Transcribes recorded audio using Groq Whisper API with Roman Urdu fintech prompt"""
    try:
        with open(AUDIO_FILE, "rb") as file:
            headers = {
                "Authorization": f"Bearer {GROQ_API_KEY}"
            }

            prompt = (
                "Only transcribe the audio in Roman Urdu (Urdu using English alphabets). "
                "Do not translate or summarize. Do not use formal English or Urdu.\n"
                "Example: Mujhe 13 number ka transaction POS mein show nahi ho raha.\n"
                "Use keywords like: POS, transaction, slip, merchant, tapsys, payment, settlement, bank, account, decline.\n"
                "Now transcribe:"
            )

            data = {
                "model": "whisper-large-v3",
                "temperature": 0,
                "response_format": "json",
                "language": "en",
                "prompt": prompt
            }

            response = requests.post(
                GROQ_TRANSCRIPTION_URL,
                headers=headers,
                data=data,
                files={"file": file}
            )

        if response.status_code == 200:
            return response.json().get("text", "No transcription found.")
        else:
            return f"Transcription failed. Status: {response.status_code}, Detail: {response.text}"

    except Exception as e:
        return f"Error: {str(e)}"
