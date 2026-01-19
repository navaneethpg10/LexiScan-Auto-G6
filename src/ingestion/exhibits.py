from src.utils.sec_client import get_json
from src.config.settings import BASE_ARCHIVES

def get_filing_index(cik, accession):
    accession = accession.replace("-", "")
    url = f"{BASE_ARCHIVES}/{int(cik)}/{accession}/index.json"
    return get_json(url)

def find_ex10_exhibits(index_json):
    return [
        f["name"]
        for f in index_json["directory"]["item"]
        if "ex-10" in f["name"].lower()
    ]
