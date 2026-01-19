import pandas as pd
from src.utils.sec_client import get_json

def load_company_ciks():
    data = get_json("https://www.sec.gov/files/company_tickers.json")
    df = pd.DataFrame.from_dict(data, orient="index")
    df["cik_str"] = df["cik_str"].astype(str).str.zfill(10)
    return df
