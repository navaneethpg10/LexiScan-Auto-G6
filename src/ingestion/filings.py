import pandas as pd
from src.utils.sec_client import get_json

def get_filings(cik):
    url = f"https://data.sec.gov/submissions/CIK{cik}.json"
    data = get_json(url)
    return pd.DataFrame.from_dict(data["filings"]["recent"])

def filter_contract_filings(df):
    return df[df["form"].isin(["10-K", "10-Q", "8-K"])]
