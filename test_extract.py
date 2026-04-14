import pdfplumber

with pdfplumber.open(r"C:\Users\dingo\Documents\Hyolmo-Nepali-English-Dictionary.pdf") as pdf:
    for i, page in enumerate(pdf.pages[:3]):  # first 3 pages only
        print(f"\n--- PAGE {i+1} ---")
        print(page.extract_text())