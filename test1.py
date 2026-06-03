import streamlit as st
import requests
from groq import Groq

# Groq API Key

st.title("🎬 AI Movie Analyzer")

movie_name = st.text_input("Enter Movie Name")

if st.button("Analyze Movie"):

    try:
        # Get Movie Data
        url = f"https://www.omdbapi.com/?t={movie_name}&apikey={OMDB_API_KEY}"

        response = requests.get(url)
        data = response.json()

        if data["Response"] == "False":
            st.error("Movie not found")
        else:

            title = data["Title"]
            year = data["Year"]
            genre = data["Genre"]
            rating = data["imdbRating"]
            plot = data["Plot"]

            st.subheader("Movie Information")

            st.write("🎥 Title:", title)
            st.write("📅 Year:", year)
            st.write("🎭 Genre:", genre)
            st.write("⭐ IMDb Rating:", rating)
            st.write("📝 Plot:", plot)

            prompt = f"""
            Analyze the movie below:

            Title: {title}
            Year: {year}
            Genre: {genre}
            IMDb Rating: {rating}

            Plot:
            {plot}

            Give:
            1. Short Summary
            2. Main Themes
            3. Who Should Watch It
            4. Similar Movies
            5. Final Recommendation
            """

            ai_response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            st.subheader("🤖 AI Analysis")

            st.write(
                ai_response.choices[0].message.content
            )

    except Exception as e:
        st.error(f"Error: {e}")