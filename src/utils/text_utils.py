from bs4 import BeautifulSoup

def extract_text_from_html(html):
    soup = BeautifulSoup(html, "lxml")
    return soup.get_text(separator=" ", strip=True)
