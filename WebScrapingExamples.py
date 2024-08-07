import os
import requests
from bs4 import BeautifulSoup
import time


# This code scrapes the website playgameoflife.com for the preset examples
#  will implement the presets into the game of life


def fetch_lexicon_page():
    url = "https://playgameoflife.com/lexicon"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.content
    else:
        print(f"Failed to fetch the lexicon page. Status code: {response.status_code}")
        return None

def extract_word_sections(soup):
    word_sections = []
    word_items = soup.select("section#presets div.item:not(.example-image)")
    for item in word_items:
        name = item.select_one("h3").text.strip()
        description = item.select_one("p").text.strip()
        word_sections.append({"name": name, "description": description})
    return word_sections

def extract_image_sections(soup):
    image_sections = []
    image_items = soup.select("section#presets div.item.example-image")
    for item in image_items:
        name = item.select_one("h3").text.strip()
        description = item.select_one("p").text.strip()
        image_url = item.select_one("img")["src"]
        image_sections.append({"name": name, "description": description, "image_url": image_url})
    return image_sections

if __name__ == "__main__":
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Create the "presets" subfolder in the script's directory if it doesn't exist
    presets_folder = os.path.join(script_dir, "presets")
    if not os.path.exists(presets_folder):
        os.makedirs(presets_folder)

    lexicon_page_content = fetch_lexicon_page()
    if lexicon_page_content:
        soup = BeautifulSoup(lexicon_page_content, "html.parser")
        word_sections = extract_word_sections(soup)
        image_sections = extract_image_sections(soup)

        # Save word sections to a file in the "presets" subfolder (name and description only)
        with open(os.path.join(presets_folder, "word_sections.txt"), "w") as f:
            for section in word_sections:
                f.write(f"{section['name']}: {section['description']}\n")

        # Save image sections to a file in the "presets" subfolder (name, description, and image URL)
        with open(os.path.join(presets_folder, "image_sections.txt"), "w") as f:
            for section in image_sections:
                f.write(f"{section['name']}: {section['description']}\n")
                f.write(f"Image URL: {section['image_url']}\n")
                f.write("\n")

        print("Presets data saved successfully in the 'presets' subfolder.")