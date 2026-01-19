from src.pipeline.extract_contracts import extract_contracts
from src.ner.model import extract_entities


def debug(cik):
    contracts_df = extract_contracts(cik, max_filings=1)

    for _, row in contracts_df.iterrows():
        print("\n========== DEBUG CONTRACT ==========")
        print("Filename:", row["filename"])
        print("\nTEXT PREVIEW:\n", row["text"][:1000])

        entities = extract_entities(row["text"])
        print("\nENTITIES:\n", entities)


if __name__ == "__main__":
    # Example: Apple Inc.
    debug("0000320193")
