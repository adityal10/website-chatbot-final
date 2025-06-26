import pandas as pd
from config import CSV_PATH

def load_website_data():
    """
    Load website content from a CSV file.

    Args:
        csv_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Cleaned DataFrame with non-empty content.
    """
    df = pd.read_csv(CSV_PATH)
    documents = []
    for _, row in df.iterrows():
        text = f"{row.get('title', '')}\n{row.get('content', '')}"
        if isinstance(text, str) and text.strip():
            documents.append(text.strip())
    return documents