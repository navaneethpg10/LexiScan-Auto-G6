import spacy
from src.ner.rules import extract_dates, extract_money, extract_termination_clauses

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)

    parties = list({ent.text for ent in doc.ents if ent.label_ in ["ORG", "PERSON"]})

    return {
        "DATES": extract_dates(text),
        "MONEY": extract_money(text),
        "PARTIES": parties,
        "TERMINATION_CLAUSES": extract_termination_clauses(text)
    }
