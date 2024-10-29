# pdf_text_explorer/pdf_extractor.py
# Wraps pdfminer.six to extract text from a PDF file.
from io import StringIO

from loguru import logger
from pdfminer.high_level import extract_text_to_fp


class PDFExtractor:
    """
    Extracts text from a PDF file.
    """
    def __init__(self):
        pass

    def extract_text(self, pdf_path):
        """
        Extracts text from a PDF file using pdfminer.six.

        Args:
            pdf_path (str): Path to the input PDF file.

        Returns:
            str: The extracted text.
        """
        try:
            logger.info(f"Extracting text from {pdf_path}")
            output_string = StringIO()
            with open(pdf_path, 'rb') as fin:
                extract_text_to_fp(fin, output_string)
            text = output_string.getvalue().strip()
            logger.info("Text extraction complete")
            return text
        except Exception as e:
            logger.error(f"Error extracting text: {e}")
            raise
