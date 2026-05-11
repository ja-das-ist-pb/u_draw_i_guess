from google import genai
import ast
from apikey import Keys

apiKey = "AIzaSyBkE5a6sW2HTuhDmBXaActTSlBiN54cgmU"
clients = [genai.Client(api_key=apikey) for apikey in Keys]

keyi = 0

response = clients[keyi].models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=content
)

print(response.text)
# print(eval(response.text[7:-3]))