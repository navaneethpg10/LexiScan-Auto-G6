import requests
from src.config.settings import HEADERS, BASE_ARCHIVES
from src.utils.text_utils import extract_text_from_html

def extract_contract_text(cik, accession, filename):
    accession = accession.replace("-", "")
    url = f"{BASE_ARCHIVES}/{int(cik)}/{accession}/{filename}"
    r = requests.get(url, headers=HEADERS)

    if filename.endswith((".htm", ".html")):
        return extract_text_from_html(r.text)
    if filename.endswith(".txt"):
        return r.text
    return None
