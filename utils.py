from paddleocr import PaddleOCR


class OCR:
    def __init__(self):
        self.model = PaddleOCR(lang='en')
        
    def perform_ocr(self, image_path):
        result = self.model.predict(image_path)
        return result[0]['rec_texts']
    
    
