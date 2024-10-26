# Whisper Model : https://huggingface.co/openai/whisper-large-v3-turbo
# Bark Model https://huggingface.co/suno/bark  # to train you own voice model
# Groq Key : https://console.groq.com/

# install these !pip install openai-whisper groq gtts gradio

# Import libraries
import whisper
import os
from gtts import gTTS
import gradio as gr
from groq import Groq

# Load Whisper model for transcription
model = whisper.load_model("base")

# Set your Groq API Key (replace with your actual key)
os.environ["GROQ_API_KEY"] = "your_groq_api_key"

# Set up Groq API client (ensure GROQ_API_KEY is set in your environment)
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY environment variable not set.")

client = Groq(api_key=api_key)


# Function to get the LLM response from Groq
def get_llm_response(user_input):
    print(f"User input for LLM: {user_input}")  # Debug: print user input
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": user_input}],
        model="llama3-8b-8192",  # Replace with your desired model
    )
    response = chat_completion.choices[0].message.content
    print(f"LLM Response: {response}")  # Debug: print LLM response
    return response


# Function to convert text to speech using gTTS
def text_to_speech(text, output_audio="output_audio.mp3"):
    print(
        f"Generating speech for: {text}"
    )  # Debug: print text to be converted to speech
    tts = gTTS(text)
    tts.save(output_audio)
    return output_audio


# Main chatbot function to handle audio input and output
def chatbot(audio):
    # Step 1: Transcribe the audio using Whisper
    print("Transcribing audio...")  # Debug: Starting transcription
    result = model.transcribe(audio)
    user_text = result["text"]
    print(f"Transcribed text: {user_text}")  # Debug: print transcribed text

    # Step 2: Get LLM response from Groq
    response_text = get_llm_response(user_text)

    # Step 3: Convert the response text to speech
    output_audio = text_to_speech(response_text)

    return response_text, output_audio


# Gradio interface for real-time interaction
iface = gr.Interface(
    fn=chatbot,
    inputs=gr.Audio(type="filepath"),  # Input from mic or file
    outputs=[
        gr.Textbox(),
        gr.Audio(type="filepath"),
    ],  # Output: response text and audio
    live=True,
)

# Launch the Gradio app
iface.launch()
