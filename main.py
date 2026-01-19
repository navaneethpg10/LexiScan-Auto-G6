from src.ingestion.cik_loader import load_company_ciks
from src.pipeline.extract_contracts import extract_contracts
from src.ner.model import extract_entities


def main():
    companies = load_company_ciks()
    cik = companies.iloc[0]["cik_str"]

    contracts_df = extract_contracts(cik)

    for _, row in contracts_df.iterrows():
        print("\n================ CONTRACT ================")
        entities = extract_entities(row["text"])

        for label, values in entities.items():
            print(f"{label}:")
            for v in values:
                print(f"  - {v}")


if __name__ == "__main__":
    main()

