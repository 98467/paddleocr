from fastapi import FastAPI , File, UploadFile
import os

from utils import OCR

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}   


@app.post("/upload")
async def receive_image(file: UploadFile=File(...)):
     
    file_path = f"temp/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    model = OCR()
    ocr_result = model.perform_ocr(file_path)
    os.remove(file_path)
    
    return {"message": "Image received", "ocr_result": ocr_result}