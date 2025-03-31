from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF resume.
    
    Args:
        pdf_path (str): Path to the PDF file.
    
    Returns:
        str: Extracted text from the PDF.
    """
    try:
        text = extract_text(pdf_path)
        return text.strip()
    except Exception as e:
        return f"Error extracting text: {str(e)}"
