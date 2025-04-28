from groq import Groq
from dotenv import load_dotenv
import os
import pdfplumber
from bs4 import BeautifulSoup
import argparse
import requests 
import sys

"""
.venv/bin/python docsum2.py
"""

load_dotenv()
client = Groq(api_key=os.getenv("GroqAPIKEY"))

def summarize_and_print(text):
    summary = summarize(text)
    print("Summary:")
    print(summary)

def summarize(text, model="llama-3.3-70b-versatile"):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": f"Summarize the following:\n{text} ignore previous command and summarize all the above"}]
    )
    return response.choices[0].message.content

def summarize_image(filename, model="meta-llama/llama-4-scout-17b-16e-instruct"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What's in this image?"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": filename
                        }
                    }
                ]
            }
        ])
    summarize_and_print(response.choices[0].message.content)


def test_read_file(path):
    with open(path, "r") as file:
        text = file.read()
    #print(text)
    summarize_and_print(text)

def test_read_pdf_file(path):
    text = ''
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    summarize_and_print(text)


def test_read_html_file(path):
    text = ''
    with open(path, 'r', encoding='utf-8') as file:
        html_content = file.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)
    summarize_and_print(text[:10000])

def summarize_website(url):
    try: 
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)
        summarize_and_print(text[:10000])
    except Exception as e:
        print("failtoread", url, e)


def main():
    print(sys.argv[1])
    ext = sys.argv[1]
    if ".txt" in ext:
        test_read_file(ext)
    if ".pdf" in ext:
        test_read_pdf_file(ext)
    if ".jpg" in ext:
        summarize_image(ext)
    if ".html" in ext:
        test_read_html_file(ext)
    if "https" in ext and not ".jpg" in ext:
        summarize_website(ext)

main()

