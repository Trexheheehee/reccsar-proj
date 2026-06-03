import streamlit as st
import speech_recognition as sr
from google import genai

# Gemini API Key
client = genai.Client(
    api_key="AIzaSyByaxWrzaV7MGJUWlsk-zpgkrp7vMENjwg"
)

st.set_page_config(page_title="Voice AI Chatbot")

st.title("🎤 Voice AI Chatbot")

if st.button("Start Recording"):

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:

            st.info("Listening... Speak now!")

            recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=10
            )

        st.success("Audio Recorded Successfully!")

        user_text = recognizer.recognize_google(audio)

        st.subheader("You Said")
        st.write(user_text)

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_text
        )

        st.subheader("AI Response")
        st.write(response.text)

    except sr.WaitTimeoutError:
        st.error("No speech detected within the time limit.")

    except sr.UnknownValueError:
        st.error("Could not understand your speech.")

    except sr.RequestError as e:
        st.error(f"Speech Recognition Service Error: {e}")

    except Exception as e:
        st.exception(e)