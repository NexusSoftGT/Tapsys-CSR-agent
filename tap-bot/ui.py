import customtkinter as ctk
import threading
import sounddevice as sd
import numpy as np
import wave
import speech
import rag
import llm
import database
import phone_lookup
import time


# ✅ UI Configuration 
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ✅ Global Variables
recording = False
audio_data = []
fs = 44100
channels = 2
AUDIO_FILE_PATH = "recorded_audio.wav"

# ✅ Hardcoded Phone Number for Now
PHONE_NUMBER = "03212430237"
merchant = phone_lookup.get_merchant(PHONE_NUMBER)
greeting = f"As-salam wa alaikum, {merchant['name']} {merchant['salutation']}! Farmayen, mein aap ke lye kya kr sakta hun?" if merchant else "As-salam wa alaikum! Farmayen, mein aap ke lye kya kr sakta hun?"

# ✅ Create Main Window
root = ctk.CTk()
root.title("🎙️ AI Transcriber & TAPSYS Support")
root.geometry("900x600")
root.state("zoomed")

# ✅ Chat Display
chat_display = ctk.CTkTextbox(root, width=800, height=500, wrap="word", font=("Arial", 16))
chat_display.pack(pady=20, padx=40, fill="both", expand=True)

# Variable to hold the entire conversation
chat_memory = []

def summarize_text(transcript):
    """Summarizes the conversation transcript"""
    # Here, you can use LLM for summarization
    summary = llm.query_llm(f"Summarize this: {transcript}")
    return summary


def update_chat(role, text):
    """Display messages in chat format and store them in memory"""
    chat_memory.append(f"{role}: {text}")
    chat_display.insert("end", f"\n\n{role}: {text}")
    chat_display.see("end")

def callback(indata, frames, time, status):
    """Buffers audio data while recording"""
    if recording:
        audio_data.append(indata.copy())

def toggle_recording():
    """Toggles recording state: starts when pressed, stops automatically when silence is detected."""
    global recording, audio_data
    if not recording:
        recording = True
        audio_data = []
        update_chat("🎙️ Me", "Recording started... Speak now!")
        threading.Thread(target=record_thread).start()
    else:
        recording = False
        update_chat("✅ Me", "Recording stopped. Processing transcription...")
        
        audio_array = np.concatenate(audio_data, axis=0)
        with wave.open(AUDIO_FILE_PATH, 'wb') as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(2)
            wf.setframerate(fs)
            wf.writeframes((audio_array * 32767).astype(np.int16).tobytes())
        
        threading.Thread(target=process_transcription).start()

def record_thread():
    """Runs recording in a separate thread and stops when silence is detected."""
    global recording
    silence_threshold = 0.01  # Silence detection threshold
    silence_duration = 2  # Seconds of silence before stopping
    silence_start = None
    
    with sd.InputStream(callback=callback, samplerate=fs, channels=channels):
        while recording:
            sd.sleep(100)
            if audio_data:
                last_chunk = np.abs(audio_data[-1]).mean()
                if last_chunk < silence_threshold:
                    if silence_start is None:
                        silence_start = time.time()
                    elif time.time() - silence_start >= silence_duration:
                        toggle_recording()
                        break
                else:
                    silence_start = None

def process_transcription():
    """Transcribes & gets AI response, handles chat memory"""
    transcript = speech.transcribe_audio()
    update_chat("🎤 Me", transcript)

    # ✅ First check RAG response
    rag_response = rag.search_rag(transcript)
    ai_response = rag_response if rag_response else llm.query_llm(transcript)

    update_chat("🤖 Bot", ai_response)

    # Check for end of conversation (e.g., "bye bye", "Allah Hafiz")
    if "bye bye" in transcript.lower() or "allah hafiz" in transcript.lower():
        
        # Summarize the conversation before saving
        summary = summarize_text(transcript)

        # Save the entire conversation as a single ticket
        phone = PHONE_NUMBER  # Assume phone number is stored in a variable
        issue = " ".join(chat_memory)  # Use the whole chat as the issue
        database.save_complaint(phone, summary, issue)
        update_chat("🤖 Bot", "Shukrya! Aapka masla darj kar diya gaya hai. Hamara numainda jald aap se raabta karega.")
        chat_memory.clear()  # Reset chat memory for the next conversation

# ✅ Display Greeting Only Once When App Starts
update_chat("🤖 Bot", greeting)

# ✅ Single Button for Auto-Start & Stop
record_button = ctk.CTkButton(root, text="🎙️ Press to Speak", command=toggle_recording, width=300)
record_button.pack(pady=20)

root.mainloop()
