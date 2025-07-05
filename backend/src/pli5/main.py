
from fastapi import FastAPI, File, UploadFile
import fitz  # PyMuPDF

app = FastAPI()

@app.post("/privacy-policy/simplify")
async def create_upload_file(file: UploadFile = File(...)):
    pdf_bytes = await file.read()
    
    text_content = ""
    
    try:
        with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
            for page in doc:
                text_content += page.get_text()
    except Exception as e:
        return {"error": f"Failed to process PDF: {e}"}

    return {"textContent": text_content}