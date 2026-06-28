import os
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai

# Configure GenAI Client
api_key = os.environ.get("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

app = FastAPI(title="Cricket Event Extractor API")

class CommentaryPayload(BaseModel):
    text: str

@app.post("/extract-events")
async def extract_events(payload: CommentaryPayload):
    if not os.environ.get("GEMINI_API_KEY"):
        raise HTTPException(status_code=500, detail="Gemini API key is not configured in environment.")

    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = (
            f"Extract critical sports metrics and milestones (such as Wickets, Boundaries, "
            f"and player half-centuries/centuries) from the following raw match commentary text. "
            f"Format the results exclusively into a valid, mini JSON array where each object "
            f"contains keys for 'over', 'event_type', and 'description'. Do not output any markdown code blocks.\n\n"
            f"Commentary text:\n{payload.text}"
        )
        
        response = model.generate_content(prompt)
        cleaned_text = response.text.strip().replace("```json", "").replace("```", "").strip()
        
        # Verify JSON validity before returning
        structured_data = json.loads(cleaned_text)
        return {"status": "success", "events": structured_data}
        
    except json.JSONDecodeError:
        return {"status": "partial_success", "raw_output": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))