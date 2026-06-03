import streamlit as st
import requests
from google import genai

# Gemini API Key
client = genai.Client(
    api_key="AIzaSyByaxWrzaV7MGJUWlsk-zpgkrp7vMENjwg"
)

# TMDB API Key
TMDB_API_KEY = "7efab5a77fa690646345faafece805f4"

st.title("🎬 AI Movie Analyzer")

movie_name = st.text_input("Enter Movie Name")

if st.button("Analyze Movie"):

    try:
        url = "https://api.themoviedb.org/3/search/movie"

        params = {
            "api_key": TMDB_API_KEY,
            "query": movie_name
        }

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        if len(data.get("results", [])) == 0:
            st.error("Movie not found")
            st.stop()

        movie = data["results"][0]

        title = movie.get("title", "N/A")
        overview = movie.get("overview", "No overview available")
        rating = movie.get("vote_average", "N/A")
        release_date = movie.get("release_date", "N/A")

        st.subheader("Movie Information")
        st.write("Title:", title)
        st.write("Rating:", rating)
        st.write("Release Date:", release_date)
        st.write("Overview:", overview)

        prompt = f"""
        Analyze this movie.

        Title: {title}
        Rating: {rating}
        Overview: {overview}

        Give:
        1. Short Summary
        2. Main Themes
        3. Who Should Watch It
        4. Similar Movies
        """

        ai_response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        st.subheader("🤖 AI Analysis")
        st.write(ai_response.text)

    except Exception as e:
        st.error(f"Error: {e}")