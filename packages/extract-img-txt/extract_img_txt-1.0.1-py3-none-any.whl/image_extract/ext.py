from PIL import Image
from pytesseract import pytesseract
from docx import Document
import re


class ImgExt():

    def __init__(self,image_path,file_name):
        self.image_path = image_path
        self.file_name = file_name

    def get_text(self):
        text = pytesseract.image_to_string(self.image_path)
        text = re.sub(r'[^\x00-\x7F]+|\x0c',' ', text)     
        return text
    def convert_to_word(self):
        document = Document()
        p = document.add_paragraph(self.get_text())
        document.save(self.file_name+".docx")
                                                

