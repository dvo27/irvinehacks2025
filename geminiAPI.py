import google.generativeai as genai

genai.configure(api_key="AIzaSyAxpK_2MdQlPoAjfFAXwAEcRsOia46o5SM")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)