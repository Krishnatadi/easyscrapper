# easyscrapper/utils.py

import re

def clean_text(text):
    """Cleans the input text by removing extra spaces and newlines."""
    return re.sub(r'\s+', ' ', text).strip()
