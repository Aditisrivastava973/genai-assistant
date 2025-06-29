import fitz  # PyMuPDF

def extract_text_from_file(file_path):
    print("📄 Attempting to extract from:", file_path)
    ext = file_path.split('.')[-1].lower()

    if ext == "pdf":
        try:
            doc = fitz.open(file_path)
            text = "\n".join([page.get_text() for page in doc])
            doc.close()
            if not text.strip():
                raise ValueError("PDF contains no readable text. It may be a scanned image.")
            return text.strip()
        except Exception as e:
            raise ValueError(f"Failed to extract PDF: {e}")

    elif ext == "txt":
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            raise ValueError(f"Failed to read TXT file: {e}")

    raise ValueError("Unsupported file format. Please upload a .pdf or .txt file.")
