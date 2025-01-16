import google.generativeai as genai

genai.configure(api_key="AIzaSyAJv_DrxNWg3B5LU2bHvB1V8cOlo0MKY0s")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)