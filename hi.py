from google import genai

client = genai.Client(
    api_key="AIzaSyByaxWrzaV7MGJUWlsk-zpgkrp7vMENjwg"
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Tell me about the movie Leo"
)

print(response.text)