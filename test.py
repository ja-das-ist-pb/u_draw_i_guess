from google import genai
import ast

apiKey = "AIzaSyBkE5a6sW2HTuhDmBXaActTSlBiN54cgmU"
client = genai.Client(api_key=apiKey)

content = """
主題：家具

我們在玩一個團隊遊戲，需要由一個人負責猜，其餘人看著題目，講出相近的意思，或者其他提示，引導猜題目的人猜中題目。

你的工作是需要提供200組針對這個題目的詞語，且不能重複。例如，以進擊的巨人為主題，您可以提供：「艾爾迪亞王國」、「始祖巨人」、「地鳴」等等類似的詞語。

請確保你只會輸出這兩百組詞語，並且這些詞語內不能有空格、將這些詞語以json格式輸出給我，並把他們裝在一個array裡面（直接從[開始輸出，並以]為輸出的最後一個字元，謝謝
"""

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=content
)

print(response.text)
print(eval(response.text[7:-3]))