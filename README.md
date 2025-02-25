# TAPSYS AI Transcriber & Support Bot

This project is a **Voice-to-Text AI Transcriber** with **24x7 support** functionality for TAPSYS, a digital fintech solution provider. The bot listens to the user's voice, transcribes it, and then provides responses based on **RAG** (Retrieval-Augmented Generation) and **LLM** (Language Learning Model) integration. It continuously listens like a normal phone call without needing to press the button multiple times, offering seamless interaction.

---

## Features

- **Real-time Voice Recording**: Continuously records the user's voice until silence is detected.
- **Real-time Transcription**: Converts the recorded audio into text in real-time using Groq’s Whisper model.
- **RAG (Retrieval-Augmented Generation)**: Fetches relevant information based on the transcription using RAG, providing relevant responses.
- **LLM (Language Learning Model) Fallback**: If RAG fails to find an answer, the bot falls back on an LLM for a response.
- **Summarization of Conversations**: After detecting the end of the conversation (e.g., "bye bye" or "Allah Hafiz"), the conversation is summarized, and a **single ticket** is created in the database with the summary.
- **24/7 Support**: The bot starts recording when prompted and automatically listens after each response to provide continuous support.

---

## Tech Stack

- **Python 3.8+**
- **CustomTkinter** (for the UI)
- **SoundDevice** (for capturing audio)
- **NumPy** (for audio processing)
- **Speech Recognition API** (for converting speech to text)
- **Groq API** (for transcription)
- **RAG + LLM** (for AI-based responses)
- **MySQL** (for storing conversation tickets)

---

## Setup & Installation

Follow these steps to set up the project on your local machine:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/tapsys-ai-transcriber.git
cd tapsys-ai-transcriber
