from fastapi import FastAPI, Request
from pydantic import BaseModel
from google import genai
import ast
from .apikey import Keys
from .content import generate_content

app = FastAPI()


clients = [genai.Client(api_key=apikey) for apikey in Keys]

class TopicRequest(BaseModel):
    topic:str


keyi = 0

@app.post("/newtopic")
def topic(req:TopicRequest):
    data = req.model_dump()
    topic = data["topic"]
    response = clients[keyi].models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=generate_content()
    )
    keyi = (keyi + 1) % len(Keys)
    
    questions = ast.literal_eval(response.text[7:-3])

    return questions

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=3333, reload=True)