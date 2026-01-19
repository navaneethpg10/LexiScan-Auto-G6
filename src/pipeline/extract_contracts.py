import pandas as pd
from src.ingestion.filings import get_filings, filter_contract_filings
from src.ingestion.exhibits import get_filing_index, find_ex10_exhibits
from src.extraction.contract_text import extract_contract_text
from src.utils.rate_limit import throttle

def extract_contracts(cik, max_filings=5):
    filings = filter_contract_filings(get_filings(cik))
    records = []

    for _, row in filings.head(max_filings).iterrows():
        accession = row["accessionNumber"]
        index = get_filing_index(cik, accession)

        for filename in find_ex10_exhibits(index):
            text = extract_contract_text(cik, accession, filename)
            if text:
                records.append({
                    "cik": cik,
                    "accession": accession,
                    "filename": filename,
                    "text": text[:15000]
                })
            throttle()

    return pd.DataFrame(records)
