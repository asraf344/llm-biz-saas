from fastapi import FastAPI  # type: ignore
from fastapi.responses import PlainTextResponse  # type: ignore
from google import genai  # type: ignore

app = FastAPI()

client = genai.Client()

@app.get("/api", response_class=PlainTextResponse)
def idea():
    prompt = "Come up with a new business idea for AI Agents"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text