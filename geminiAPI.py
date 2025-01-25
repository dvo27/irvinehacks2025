# import google.generativeai as genai
from inference_sdk import InferenceHTTPClient

CLIENT = InferenceHTTPClient(
    api_url="X2ztjBd1fkNwfVwJKQKv",
    api_key="API_KEY"
)

result = CLIENT.infer(samplefridgeimage.jpeg, model_id="aicook-lcv4d/3")
print(result)

# genai.configure(api_key="AIzaSyAxpK_2MdQlPoAjfFAXwAEcRsOia46o5SM")
# model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("Explain how AI works")
# print(response.text)