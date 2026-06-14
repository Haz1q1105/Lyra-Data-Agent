from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

apikey = os.getenv("MY_SECRET_KEY")

client = genai.Client(api_key=apikey)

# Request a response
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='Explain agentic AI in data science using exactly one sentence.'
)

# 4. Print results
print("\n--- GOOGLE RESPONSE ---")
print(response.text)