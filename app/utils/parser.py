from pdfminer.high_level import extract_text as extract_pdf_text
from docx import Document
import os

def extract_text_from_resume(file_storage):
    """
    Extracts raw text from an uploaded resume (PDF or DOCX).
    Returns: extracted text as a string.
    """
    filename = file_storage.filename.lower()

    if filename.endswith(".pdf"):
        return _extract_text_from_pdf(file_storage)
    elif filename.endswith(".docx"):
        return _extract_text_from_docx(file_storage)
    else:
        raise ValueError("Unsupported file format. Please upload a PDF or DOCX resume.")

def _extract_text_from_pdf(file_storage):
    temp_path = "temp_resume.pdf"
    file_storage.save(temp_path)

    try:
        text = extract_pdf_text(temp_path)
    finally:
        os.remove(temp_path)

    return text.strip()

def _extract_text_from_docx(file_storage):
    temp_path = "temp_resume.docx"
    file_storage.save(temp_path)

    try:
        doc = Document(temp_path)
        text = "\n".join([para.text for para in doc.paragraphs])
    finally:
        os.remove(temp_path)

    return text.strip()
