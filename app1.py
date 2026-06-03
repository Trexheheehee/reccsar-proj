from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Read API key from .env file
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)

print("🤖 Gemini Chatbot")
print("Type 'exit' to quit.\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input
        )

        print("\nBot:", response.text)
        print()

    except Exception as e:
        print("Error:", e)