# LLM Project

This script uses the Groq LLM to summarize contents of various files, including `.jpg`, `.html`, `.txt`, `.pdf`, and websites.

---

## 🔧 How to Use

In the terminal, run the following commands depending on the input file type:

### 📄 HTML File

python3 docsum.py docs/news-mx.html

Example Output:
---------------
File Type: HTML  
Summary:  
The article discusses recent political developments in Mexico, highlighting key reforms and public response.

---

### 📝 Text File

python3 docsum.py docs/constitution-mx.txt

Example Output:
---------------
File Type: TXT  
Summary:  
The Mexican Constitution outlines the federal structure, individual rights, and responsibilities of the state.

---

### 📚 PDF File

python3 docsum.py docs/research_paper.pdf

Example Output:
---------------
File Type: PDF  
Summary:  
This research paper analyzes the effects of economic policy on rural development in Latin America.

---

### 🌐 Website URL

python3 docsum.py https://elpais.com/us/

Example Output:
---------------
File Type: Webpage  
Summary:  
El País (US edition) provides coverage of international news, politics, and cultural events.

---

### 🖼️ JPG Image

python3 docsum.py https://www.cmc.edu/sites/default/files/about/images/20170213-cube.jpg

Example Output:
---------------
File Type: Image (JPG)  
Summary:  
The image depicts the CMC Cube sculpture, a prominent feature on the Claremont McKenna College campus.

---

## 📦 Dependencies

Install required packages with:

pip install groq pdfplumber beautifulsoup4 requests

---

## 🧠 Powered by

- Groq API (https://groq.com/)
- Python 3.9+
