from fastapi import FastAPI  # type: ignore
from fastapi.responses import StreamingResponse  # type: ignore

from google import genai  # type: ignore

app = FastAPI()

client = genai.Client()

@app.get("/api")
def idea():
    prompt = "Come up with a new business idea for AI Agents"
    stream = client.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents=prompt
    )

    def event_stream():
        for chunk in stream:
            text = chunk.text
            if text:
                lines = text.split("\n")
                for line in lines:
                    yield f"data: {line}\n"
                yield "\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")
