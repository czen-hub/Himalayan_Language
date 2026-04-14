from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import json
from urllib.parse import quote

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Devanagari letters
letters = [
    'आ','इ','उ','ऊ','ए','ऐ','ओ','औ','क','ख','ग','घ','ङ','च','छ',
    'ज','भ','ट','ठ','ड','ह','त','थ','द','ध','न','प','फ','ब','म',
    'य','र','ल','व','स','ह'
]

def scrape_entries():
    words = []
    entries = driver.find_elements(By.CLASS_NAME, "entry")
    for entry in entries:
        try:
            try:
                word = entry.find_element(By.CLASS_NAME, "mainheadword").text.strip()
            except:
                word = ""
            try:
                pronunciation = entry.find_element(By.CLASS_NAME, "pronunciation").text.strip()
            except:
                pronunciation = ""
            try:
                pos = entry.find_element(By.CLASS_NAME, "partofspeech").text.strip()
            except:
                pos = ""
            try:
                meaning = entry.find_element(By.CLASS_NAME, "sensecontent").text.strip()
            except:
                meaning = ""
            if word:
                words.append({
                    "original_word": word,
                    "pronunciation": pronunciation,
                    "part_of_speech": pos,
                    "english_meaning": meaning,
                    "language": "hyolmo"
                })
        except Exception as e:
            print(f"Error: {e}")
    return words

all_words = []

for letter in letters:
    encoded = quote(letter)
    page = 1
    while True:
        url = f"https://www.webonary.org/hyolmo/browse/browse-vernacular-nepali/?key=scp-fonipa-x-etic&letter={encoded}&lang=en&pagenr={page}"
        driver.get(url)
        time.sleep(2)
        words = scrape_entries()
        print(f"Letter {letter} page {page} → {len(words)} words")
        if len(words) == 0:
            break
        all_words.extend(words)
        page += 1

print(f"\nTotal: {len(all_words)} words scraped")

with open("hyolmo_words.json", "w", encoding="utf-8") as f:
    json.dump(all_words, f, ensure_ascii=False, indent=2)

print("Saved to hyolmo_words.json")
driver.quit()