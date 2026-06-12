from dotenv import load_dotenv
from google import genai
from google.genai import types
load_dotenv()
Client=genai.Client()
def analyze_resume(system_prompt, user_prompt):
    response=Client.models.generate_content(
         model="models/gemini-flash-latest",
         contents=user_prompt,
         config=types.GenerateContentConfig(
             system_instruction=system_prompt,
             max_output_tokens=8000,
             temperature=0.2,
             response_mime_type="application/json"
         ),
         
     )
    return response[0].text