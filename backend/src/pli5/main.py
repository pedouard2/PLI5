from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from fpdf import FPDF
from pydantic import BaseModel
import os

app = FastAPI()

# --- CORS Middleware ---
origins = ["http://localhost:5173", "http://127.0.0.1:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PrivacyPolicyRequest(BaseModel):
    text: str

def create_pdf_from_text(text: str) -> bytes:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.set_text_color(0,0,0)
    pdf.cell(0, 10, "Test PDF", ln=1)
    
    output = pdf.output()

    
    return bytes(output)

@app.post("/privacy-policy/simplify")
async def simplify_privacy_policy(payload: PrivacyPolicyRequest):
    """Receives text, creates a PDF in memory, and returns it."""
    try:
        pdf_bytes = create_pdf_from_text(payload.text)
        if isinstance(pdf_bytes, bytearray):
            pdf_bytes = bytes(pdf_bytes)
        headers = {
            'Content-Disposition': 'attachment; filename="simplified_policy.pdf"'
        }
        
        return Response(content=pdf_bytes, media_type='application/pdf', headers=headers)

    except Exception as e:

        raise HTTPException(status_code=500, detail=f"Failed to create PDF: {e}")