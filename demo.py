# STREAMLIT VERSION OF demo2.py
# TEXT TO SPEECH APPLICATION

import streamlit as st
import os
from google.cloud import texttospeech_v1
from google.cloud import texttospeech

# Set Google Cloud credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'sa_text_demo.json'

# Initialize Streamlit app
st.title("Text to Speech App")

text = st.text_area("Enter the text to convert to speech")

if st.button("Convert to Speech"):
    client = texttospeech_v1.TextToSpeechClient()

    synthesis_input = texttospeech_v1.SynthesisInput(text=text)

    voice1 = texttospeech_v1.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech_v1.SsmlVoiceGender.MALE
    )

    audio_config = texttospeech_v1.AudioConfig(
        audio_encoding=texttospeech_v1.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice1,
        audio_config=audio_config
    )

    audio_file = response.audio_content
    audio = st.audio(audio_file, format="audio/wav")
    
            
    # with open("audio.wav", "rb") as file:
    #     btn = st.download_button(
    #         label="Download Audio File",
    #         data=file,
    #         file_name="audio.wav",
    #         mime="audio/wav"
    #     )

if __name__ == '__main__':
    st.write("Enter the text and click the 'Convert to Speech' button to synthesize speech.")
