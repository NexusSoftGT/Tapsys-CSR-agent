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
```


### 2. Install Python dependencies
Create a virtual environment and install the required dependencies.

```bash
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# Install the required libraries
pip install -r requirements.txt
```

### 3. Setup the Database
Install MySQL (if not already installed).
Set up the MySQL database for storing tickets:
Run the following SQL command in phpMyAdmin or MySQL Workbench to create the necessary tables:

```bash
CREATE DATABASE tapsys_db;

USE tapsys_db;

CREATE TABLE complaints (
    id INT AUTO_INCREMENT PRIMARY KEY,
    phone VARCHAR(255),
    issue TEXT,
    transcript TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Usage
1. Start the Application
Run the Python script to launch the AI Transcriber & TAPSYS Support Bot.
`python ui.py`

## 2. How the Bot Works
Press the "Press to Speak" button to start the interaction.
Speak your issue.
The bot will transcribe your voice into text, generate a response using RAG or LLM, and then continue listening for the next issue until the conversation ends.
If the conversation ends (with "bye bye" or "Allah Hafiz"), the entire conversation is saved as a single ticket in the MySQL database with the summary.

# Folder Structure

```bash
/tapsys-ai-transcriber
│
├── ui.py                # Main UI application (Tkinter)
├── database.py          # Database connection and functions
├── speech.py            # Speech-to-text functions
├── rag.py               # Retrieval-Augmented Generation functions
├── llm.py               # Language Model functions for fallback
├── phone_lookup.py      # Hardcoded merchant lookup (to be replaced with real DB)
├── requirements.txt     # List of dependencies
└── README.md            # Project overview and instructions
```

## Configuration
### 1. Database Configuration
Make sure your MySQL database is configured correctly and the credentials are updated in database.py.

### 2. Phone Lookup
Currently, a hardcoded phone number and merchant lookup is used. Replace it with an actual database or API call if needed.
